---
applyTo: '**'
---

# Python Testing Rules

## Core Testing Principles

### Always Write Tests
Every new feature or bug fix must include corresponding tests.
Generate tests in separate files never put two or more tests in the same file.
### Test First Approach
Consider writing tests before implementation (TDD) when appropriate.

### Test Coverage Target
Maintain minimum 80% test coverage for critical code paths.

## Test Organization Rules

### File Naming Convention
- Test files must use `test_*.py` naming pattern
- Test files must mirror source file structure

### Test Function Rules
- Each test function must test exactly one behavior
- Test function names must be descriptive and specific
- Use `test_` prefix for all test functions

## Test Content Rules

### Required Test Types
- Unit tests for individual functions/classes
- Integration tests for module interactions
- Edge case tests for boundary conditions

### Test Structure Rules
- Must follow Arrange-Act-Assert pattern
- Must include clear assertions
- Must not contain business logic

## Test Quality Rules

### Test Independence
- Tests must not depend on other tests
- Each test must setup its own data
- Tests must clean up after themselves

### Test Performance
- Unit tests must execute in <100ms
- Integration tests must execute in <1s
- Use mocking to avoid external dependencies

## Test Maintenance Rules

### Test Updates
- Tests must be updated when code changes
- Obsolete tests must be removed
- Test documentation must be maintained

### Test Review
- All tests must be code reviewed
- Test coverage must be verified before merge
- Test failures must block deployment