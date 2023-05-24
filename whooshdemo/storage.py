from whoosh.filedb.filestore import FileStorage

# open_dir 和 create_in 就是封装的这个类实现的。
storage = FileStorage('indexdir')

# idx = storage.create_index(schema)
idx = storage.open_index()

