#!/usr/bin/env python3
"""PostgreSQL Query MCP Server for Kilo Code.

This MCP server provides tools to execute SQL queries against a PostgreSQL database.
"""
import json
import logging
import os
import sys
from typing import Any

import psycopg2
from psycopg2.extras import RealDictCursor
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")
MAX_ROWS = int(os.environ.get("MAX_ROWS", "100"))
server = Server("postgres-query-server")

def get_connection():
    """Create and return a database connection."""
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable is required")
    return psycopg2.connect(DATABASE_URL)


def execute_query(query: str, params: tuple | None = None) -> dict[str, Any]:
    """Execute a SQL query and return results."""
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                if cursor.description:
                    columns = [desc[0] for desc in cursor.description]
                    rows = cursor.fetchmany(MAX_ROWS)
                    row_count = cursor.rowcount
                    return {
                        "success": True,
                        "columns": columns,
                        "rows": [dict(row) for row in rows],
                        "row_count": row_count,
                        "truncated": row_count > MAX_ROWS
                    }
                conn.commit()
                return {
                    "success": True,
                    "affected_rows": cursor.rowcount,
                    "message": "Query executed successfully"
                }
    except psycopg2.Error as e:
        logger.error("Database error: %s", e)
        return {
            "success": False,
            "error": str(e),
            "error_code": e.pgcode if hasattr(e, 'pgcode') else None
        }

@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="execute_query",
            description="Execute a SQL query against the PostgreSQL database. Use for SELECT, INSERT, UPDATE, DELETE operations.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The SQL query to execute"
                    }
                },
                "required": ["query"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls."""
    if name == "execute_query":
        query = arguments.get("query", "")
        result = execute_query(query)
        return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
    return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]


async def main():
    """Run the MCP server."""
    logger.info("Starting PostgreSQL Query MCP Server")
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
