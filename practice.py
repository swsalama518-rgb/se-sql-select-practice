import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

product_data = pd.read_sql("""
SELECT *
  FROM products;
""", conn)

print(product_data)
product_names_and_codes = pd.read_sql("""
SELECT productName, productCode
  FROM products;
""", conn).tail()

print(product_names_and_codes)

product_names_and_codes = pd.read_sql("""
SELECT productCode, productName
  FROM products;
""", conn).tail()

print(product_names_and_codes)  

product_by_line = pd.read_sql("""
SELECT productLine, productName,
case
WHEN productLine = "Planes" THEN "Planes"
ELSE "Not Planes"
END AS Planes
  FROM products;
""", conn)

print(product_by_line)

product_description_length = pd.read_sql("""
SELECT LENGTH(productDescription) AS description_length
  FROM products;
""", conn)

print(product_description_length)

products_upper_vendors = pd.read_sql("""
SELECT UPPER(productVendor) AS caps_vendor
  FROM products;
""", conn).head()

print(products_upper_vendors)
product_names_lower = pd.read_sql("""
SELECT lower(productName) AS lower_name
  FROM products;
""", conn).head()


print(product_names_lower)
product_scales = pd.read_sql("""
SELECT substr(productScale, 3,3) AS non
  FROM products;
""", conn)

print(product_scales)
products_with_vendors = pd.read_sql("""
SELECT productVendor || " " || productName AS fullName
  FROM products;
""", conn)

print(products_with_vendors)
rounded_price_diffs = pd.read_sql("""
SELECT CAST(round(MSRP - buyPrice) AS INTEGER) AS round_diff
  FROM products;
""", conn)

print(rounded_price_diffs)
conn.close()
