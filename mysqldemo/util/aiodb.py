import aiomysql
from config import *


class AIODB:
    '''
    异步数据库操作类
    '''

    pool = None

    @classmethod
    async def init(cls, loop):
        '''
        数据库初始化。
        '''

        if cls.pool is None:
            cls.pool = await aiomysql.create_pool(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASS,
                # db=DB_NAME,
                loop=loop
            )
        return cls.pool

    @classmethod
    async def quit(cls):
        '''
        数据库释放
        '''

        if cls.pool != None:
            cls.pool.close()
            await cls.pool.wait_closed()
            cls.pool = None

    @classmethod
    async def find(cls, sql):
        '''
        执行查询获取多行数据
        '''
        
        async with cls.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql)
                return await cur.fetchall()

    @classmethod
    async def find_one(cls, sql):
        '''
        执行查询获取单行数据
        '''

        async with cls.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql)
                return await cur.fetchone()

    @classmethod
    async def exec(cls, sql, commit=False):
        '''
        执行语句
        '''

        async with cls.pool.acquire() as conn:
            async with conn.cursor() as cur:
                r = await cur.execute(sql)
                if not commit:
                    return r
            await conn.commit()
            return r

    @classmethod
    async def list_schemas(cls):
        '''
        列举数据库
        '''

        dbs = await cls.find(f"SHOW DATABASES")
        return [db[0] for db in dbs]

    @classmethod
    async def list_schema_like(cls, v):
        '''
        模糊列举数据库
        '''

        dbs = await cls.find(f"SHOW DATABASES LIKE '{v}'")
        return [db[0] for db in dbs]

    @classmethod
    async def list_tables(cls):
        '''
        列举表
        '''

        ts = await cls.find(f"SHOW TABLES")
        return [t[0] for t in ts]

    @classmethod
    async def list_table_like(cls, v):
        '''
        模糊列举表
        '''

        ts = await cls.find(f"SHOW TABLES LIKE '{v}'")
        return [t[0] for t in ts]

    @classmethod
    async def list_columns(cls, t):
        '''
        列举表的字段
        '''

        cs = await cls.find(f"SHOW COLUMNS FROM `{t}`")
        return [r[0] for r in cs]

    async def list_column_like(cls, t, v):
        '''
        模糊列举表的字段
        '''
        
        cs = await cls.find(f"SHOW COLUMNS FROM `{t}` LIKE '{v}'")
        return [r[0] for r in cs]

    @classmethod
    async def list_columns_info(cls, t):
        '''
        模糊列举表的字段信息
        '''

        cs = await cls.find(f"SHOW COLUMNS FROM `{t}`")
        return [{'field': r[0], 'type': r[1], 'null': r[2], 'key': r[3], 'default': r[4], 'extra': r[5]} for r in cs]

    @classmethod
    async def use_schema(cls, name):
        '''
        选中数据库
        '''

        await cls.exec(f"USE {name}")

    @classmethod
    async def exists_table_like(cls, v):
        '''
        表是否存在
        '''

        ts = await cls.find(f"SHOW TABLES LIKE '{v}'")
        return ts != None and len(ts) > 0

    @classmethod
    async def exists_column_like(cls, t, v):
        '''
        表的字段是否存在
        '''

        cs = await cls.find(f"SHOW COLUMNS FROM `{t}` LIKE '{v}'")
        return cs != None and len(cs) > 0

    @classmethod
    async def add_column(cls, t, name, define):
        '''
        添加表字段
        '''

        await cls.exec(f"ALTER TABLE `{t}` ADD COLUMN {name} {define}")
