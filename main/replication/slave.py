from pymysqlreplication import BinLogStreamReader

mysql_settings = {'host': '127.0.0.1', 'port': 3306, 'user': 'replicator', 'passwd': '123456'}

stream = BinLogStreamReader(connection_settings = mysql_settings, server_id=100)

for (i, binlogevent) in enumerate(stream):
    print(i)
    print(binlogevent.__dict__)

stream.close()