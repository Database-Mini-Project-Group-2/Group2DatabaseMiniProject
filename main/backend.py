import pandas as pd
import pypyodbc as odbc
from sqlalchemy import create_engine, URL

# Connection -----------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------


sql_statement = """
    SELECT sr.Name FROM Sales.SalesOrderHeader soh
    JOIN Sales.SalesOrderHeaderSalesReason sohsr ON soh.SalesOrderID = sohsr.SalesOrderID
    JOIN Sales.SalesReason sr ON sohsr.SalesReasonID = sr.SalesReasonID 
"""
df = pd.read_sql_query(sql_statement, engine)


sql_sales = """
    SELECT soh.OrderDate, COUNT(*) total
    FROM Sales.SalesOrderHeader soh 
    JOIN Sales.Customer c ON soh.CustomerID = c.CustomerID 
    JOIN Sales.Store s ON s.BusinessEntityID = c.StoreID 
    JOIN Sales.SalesOrderDetail sod ON sod.SalesOrderID = soh.SalesOrderID
    JOIN Sales.SpecialOfferProduct sop ON sod.ProductID = sop.ProductID
    JOIN Production.Product p ON p.ProductID = sop.ProductID
    JOIN Person.Address a ON soh.ShipToAddressID = a.AddressID
    GROUP BY soh.OrderDate
    ORDER BY OrderDate ASC
"""
sales_df = pd.read_sql_query(sql_sales, engine)


sales_person = """
    SELECT p.LastName, p.FirstName, sp.SalesLastYear, sp.SalesYTD
    FROM Sales.SalesPerson sp 
    JOIN HumanResources.Employee e ON sp.BusinessEntityID = e.BusinessEntityID
    JOIN Person.Person p ON e.BusinessEntityID = p.BusinessEntityID
    ORDER BY SalesLastYear DESC
"""
sales_person_df = pd.read_sql_query(sales_person, engine)


store_names = """
    SELECT DISTINCT Name FROM Sales.Store
"""
store_names_df = pd.read_sql_query(store_names, engine)


store_table_df = pd.DataFrame(
    {
        "product Name": ["Dent", "Prefect", "Beeblebrox", "Astra"],
    }
)