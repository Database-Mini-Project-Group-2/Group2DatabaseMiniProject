import pypyodbc as odbc
from sqlalchemy import create_engine, URL

# Local SQL Server for AdventureWorks2016 Database
MOKGETHWA_SERVER_NAME = 'MOKGETHWA'
SAM_SERVER_NAME = 'SAM-PC\\SQLEXPRESS'

connection_string = f"""
    Driver={{SQL Server}};
    Server={SAM_SERVER_NAME};
    Database=AdventureWorks2016;
    Trusted_Connection=yes;
"""
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url, module=odbc)
