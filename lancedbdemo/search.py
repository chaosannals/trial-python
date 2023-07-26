import lancedb

uri = "./.lancedb"
db = lancedb.connect(uri)
table = db.open_table("my_table")
result = table.search([100, 100]).limit(2).to_df()
print(result)
df = table.to_pandas()
print(df)
