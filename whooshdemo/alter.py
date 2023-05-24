from whoosh.index import open_dir
from whoosh.sorting import add_sortable, FieldFacet
from whoosh.fields import TEXT, ID, DATETIME

idx = open_dir("indexdir")

# 这样查询会缺少 动态字段定义
items = idx.schema.items()
print(items)
# 这样查询会缺少 动态字段定义
fields = idx.schema.names()
print(fields)

writer = idx.writer()
# 添加字段，只能添加一次，再次添加会报错
# 不设置成 stored=True 没报保留原数据，只做了索引。
if not 'aaaa' in fields:
    writer.add_field('aaaa', TEXT)

# 动态字段 必须指定 glob=True 和命名时使用 * ? 或者 [abc]
# if not 'dyn_*' in fields:
#     writer.add_field('dyn_*', TEXT(stored=True), glob=True)
# 移除动态字段必须和添加时命名一致
# writer.remove_field('dyn_*')

# 添加排序
add_sortable(writer, "title", FieldFacet('title'))

if not 'anthor' in fields:
    writer.add_field('anthor', TEXT(stored=True))

if not 'address' in fields:
    writer.add_field('address', TEXT(stored=True))

if not 'create_at' in fields:
    writer.add_field('create_at', DATETIME(stored=True))

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