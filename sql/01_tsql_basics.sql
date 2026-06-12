/*
Purpose:
- Validate local SQL Server setup on macOS.
- Demonstrate SQL Server connection using Docker + VS Code.
- Used to follow T-SQL tutorials and Azure SQL examples.

Environment:
- Docker Desktop
- azure-sql-edge container
- VS Code + Microsoft MSSQL extension
- SQL Server accessible via localhost:1433
*/

-- Connection test
SELECT 'Hello, T-SQL!' AS Message;

-- Current date and time
SELECT GETDATE() AS CurrentDateTime;

-- Basic arithmetic
SELECT
    10 + 20 AS Addition,
    50 - 15 AS Subtraction;

-- Variables
DECLARE @Name VARCHAR(50) = 'Sushmitha';
SELECT @Name AS StudentName;