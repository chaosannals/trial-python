import asyncio
from util.aiodb import AIODB
from config import *

async def main(loop):
    '''

    '''
    await AIODB.init(loop)
    dbs = await AIODB.list_schema_like(DB_NAME_LIKE)
    for db in dbs:
        await AIODB.use_schema(db)
        print(f'use db: {db}')
        if await AIODB.exists_table_like(DB_ADDFIELD_TABLE):
            for (f, d) in DB_ADDFIELD_COLUMNS.items():
                if await AIODB.exists_column_like(DB_ADDFIELD_TABLE, f):
                    print(f'{db}.{DB_ADDFIELD_TABLE} exists: {f}')
                else:
                    await AIODB.add_column(DB_ADDFIELD_TABLE, f, d)
                    print(f'add field {f} to {db}.{DB_ADDFIELD_TABLE}')
                    

    await AIODB.quit()


if '__main__' == __name__:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main(loop))
    except KeyboardInterrupt:
        pass
