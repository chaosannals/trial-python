from whoosh.index import open_dir
from whoosh.fields import TEXT, ID

idx = open_dir("indexdir")
writer = idx.writer()
# 添加字段，只能添加一次，再次添加会报错
# 不设置成 stored=True 没报保留原数据，只做了索引。
writer.add_field('aaaa', TEXT)

# 动态字段 必须指定 glob=True 和命名时使用 * ? 或者 [abc]
writer.add_field('dyn_*', TEXT(stored=True), glob=True)
# 移除动态字段必须和添加时命名一致
# writer.remove_field('dyn_*')

writer.add_field('anthor', TEXT(stored=True))
writer.add_field('address', TEXT(stored=True))

# writer.add_document(
#     title=u"First document, 中文",
#     path=u"/path/to/dddd",
#     content=u"dyn this first doc 带中文信息",
#     # 动态字段命名命中就可以添加。
#     dyn_aaaa="动态字段2",
#     dyn_bbbb="动态字段1",
# )

# 提交修改 可以设置优化索引，数据大时应该会耗时很大。会把文件合并成一个。
# writer.commit(optimize=True)
writer.commit()
# 取消修改
# writer.cancel()