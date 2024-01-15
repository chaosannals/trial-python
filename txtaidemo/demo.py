# 嵌入数据库示例

from txtai.embeddings import Embeddings

embeddings = Embeddings({"path": "sentence-transformers/all-MiniLM-L6-v2"})
embeddings.index([(0, "Correct", None), (1, "Not what we hoped", None)])
r = embeddings.search("positive", 1)
print(r)