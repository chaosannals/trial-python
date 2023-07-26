import lancedb

uri = "./.lancedb"
db = lancedb.connect(uri)
table = db.open_table("my_table")

# table.delete("createAt = '1690358416394516300'") # 此条莫名失败了。Column createat does not exist in the dataset
table.delete("item = 'foo'")

df = table.to_pandas()
print(df)
