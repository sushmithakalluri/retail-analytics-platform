# Local Development Setup

## SQL Server (T-SQL)

### Prerequisites
- Docker Desktop
- VS Code
- SQL Server (mssql) extension

### Start SQL Server
1. Open Docker Desktop.
2. Start the `sql` container.
3. Verify port mapping is `1433:1433`.

### Connect from VS Code
1. Press `Cmd + Shift + P`.
2. Select `MS SQL: Connect`.

Use:
- Server: `localhost`
- Authentication: `SQL Login`
- User: `sa`
- Database: `master`
- Trust Server Certificate: `Yes`

### Test Query

SELECT 'Hello, T-SQL!' AS Message;
