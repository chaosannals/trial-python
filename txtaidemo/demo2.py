from txtai.embeddings import Embeddings

# TODO 找个支持中文的模型。
# sentence-transformers/nli-mpnet-base-v2 中文结果好差。
embeddings = Embeddings(path="sentence-transformers/nli-mpnet-base-v2")

data = [
    "US tops 5 million confirmed virus cases",
    "Canada's last fully intact ice shelf has suddenly collapsed, forming a Manhattan-sized iceberg",
    "Beijing mobilises invasion craft along coast as Taiwan tensions escalate",
    "The National Park Service warns against sacrificing slower friends in a bear attack",
    "Maine man wins $1M from $25 lottery ticket",
    "Make huge profits without work, earn up to $100,000 a day",
    "缅因州男子从25美元的彩票中赢得100万美元."
]

# 文本索引
embeddings.index(data)

print(f"{'Query':20} 最匹配")
print("-" * 50)

# 遍历所有关键词，逐个调用搜索
for query in ("feel good story", "climate change", "public health story", "war",
              "wildlife", "asia", "lucky", "dishonest junk", "幸运", "骗子", "野生动物"):
    # 提取第一个结果
    # 结果格式: (uid, score)
    uid = embeddings.search(query, 1)[0][0]

    # 打印结果
    print(f"{query:20} {data[uid]}")
