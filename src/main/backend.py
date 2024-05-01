import pandas as pd

from connection import engine as conn

sql_statement = """
    SELECT sr.Name FROM Sales.SalesOrderHeader soh
    JOIN Sales.SalesOrderHeaderSalesReason sohsr ON soh.SalesOrderID = sohsr.SalesOrderID
    JOIN Sales.SalesReason sr ON sohsr.SalesReasonID = sr.SalesReasonID 
"""
df = pd.read_sql_query(sql_statement, conn)

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
sales_df = pd.read_sql_query(sql_sales, conn)

sales_person = """
    SELECT p.LastName, p.FirstName, sp.SalesLastYear, sp.SalesYTD
    FROM Sales.SalesPerson sp 
    JOIN HumanResources.Employee e ON sp.BusinessEntityID = e.BusinessEntityID
    JOIN Person.Person p ON e.BusinessEntityID = p.BusinessEntityID
    ORDER BY SalesLastYear DESC
"""
sales_person_df = pd.read_sql_query(sales_person, conn)

store_names = """
    SELECT distinct Name FROM Sales.Store
"""
store_names_df = pd.read_sql_query(store_names, conn)
# store_dropdown_options = [{'label': str(val), 'value': val} for val in store_names_df['name'].unique()]
