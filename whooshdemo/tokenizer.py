from whoosh.analysis import RegexTokenizer
from faker import Faker

fake = Faker(['zh_CN', 'en_US'])

# 这个分词器不适合中文
tokenizer = RegexTokenizer()
for token in tokenizer(fake.text()):
    print(token.text)

