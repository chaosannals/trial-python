import datetime

n = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
n11 = datetime.datetime.strptime(n, '%Y-%m-%d %H:%M:%S')

print(n)
print(n11)

n2 = datetime.date.today().strftime('%Y-%m-%d')
n22 = datetime.datetime.strptime(n2, '%Y-%m-%d').date()
n33 = datetime.datetime.strptime('2020-02-01', '%Y-%m-%d').date()

print(n2)
print((n22 - n33).days)
print(n22 + datetime.timedelta(days=2))

# d1 = datetime.datetime.strptime(datetime.date.today().strftime('%Y-%m-%d'), '%Y-%m-%d')
d1 = datetime.date.today()
print(d1)