from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)

mysql_settings = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'replicator',
    'passwd': '123456'
}
# log-bin=mysql-bin
# server-id=1
# binlog-format=ROW
# enforce_gtid_consistency=ON
# gtid_mode=ON
# log-slave_updates=true

stream = BinLogStreamReader(
    connection_settings=mysql_settings,
    only_events=[
        DeleteRowsEvent,
        WriteRowsEvent,
        UpdateRowsEvent
    ],
    blocking=False,
    server_id=100
)

for (i, binlogevent) in enumerate(stream):
    print(i)
    print(binlogevent.dump())
    for row in binlogevent.rows:
        if isinstance(binlogevent, DeleteRowsEvent):
            print(dict(row['values'].items()))
        elif isinstance(binlogevent, UpdateRowsEvent):
            print(dict(row['before_values'].items()))
            print(dict(row['after_values'].items()))
        elif isinstance(binlogevent, WriteRowsEvent):
            print(dict(row['values'].items()))

stream.close()
