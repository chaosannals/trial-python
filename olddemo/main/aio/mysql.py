import asyncio
import aiomysql


async def fetchall(sql, loop):
    async with aiomysql.create_pool(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        db='trial',
        loop=loop
    ) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql)
                return await cur.fetchall()

async def main(loop):
    '''
    '''
    a = await fetchall('SELECT * FROM t_user', loop)
    print(a)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
