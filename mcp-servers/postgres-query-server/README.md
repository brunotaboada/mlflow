# PostgreSQL Query MCP Server

A Model Context Protocol (MCP) server that provides tools to execute SQL queries against a PostgreSQL database.

## Features

- **execute_query**: Execute any SQL query (SELECT, INSERT, UPDATE, DELETE)
- **list_tables**: List all tables in the database
- **get_table_schema**: Get column information for a specific table
- **test_connection**: Test the database connection

## Installation

1. Create a virtual environment and install dependencies:

```bash
cd mcp-servers/postgres-query-server
python -m venv .venv
.venv\Scripts\activate  # Windows
# or: source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

2. Set up your environment variables:

Create a `.env` file in the project root or set the environment variable:

```bash
POSTGRES_DATABASE_URL=postgresql://user:password@host:port/database
```

## Configuration

The MCP server is configured in `.kilocode/mcp.json`:

```json
{
  "mcpServers": {
    "postgres-query": {
      "command": "python",
      "args": ["mcp-servers/postgres-query-server/server.py"],
      "env": {
        "DATABASE_URL": "${POSTGRES_DATABASE_URL}",
        "MAX_ROWS": "100"
      }
    }
  }
}
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `MAX_ROWS` | Maximum rows to return from queries | 100 |

## Usage Examples

Once configured, you can use the tools through Kilo Code:

### Test Connection
```
Test the database connection
```

### List Tables
```
List all tables in the database
```

### Get Table Schema
```
Get the schema for the users table
```

### Execute Query
```
Execute: SELECT * FROM users LIMIT 10
```

## Security Notes

- Never commit your `.env` file or database credentials
- The server limits query results to prevent memory issues
- Use read-only database users when possible for safety
