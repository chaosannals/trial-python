from whoosh.analysis import RegexTokenizer, NgramTokenizer
from faker import Faker

fake = Faker(['zh_CN', 'en_US'])

# 这个分词器不适合中文
tokenizer = RegexTokenizer()
for token in tokenizer(fake.text()):
    print(token.text)

# 适用于电话号码，编号切词。
ngram = NgramTokenizer(minsize=1, maxsize=13)
for token in ngram(fake.name()):
    print(token.text)