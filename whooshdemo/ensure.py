from whoosh.index import exists_in

# 只是比 open_dir 多了个目录判断。
idx = exists_in('indexdir')