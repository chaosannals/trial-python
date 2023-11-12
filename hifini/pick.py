import re
import os
import asyncio
import httpx
from bs4 import BeautifulSoup

TITLE_PATTERN = re.compile(r"title\s*:\s*'(.+?)',")
AUTHOR_PATTERN = re.compile(r"author\s*:\s*'(.+?)',")
MUSIC_KEY_PATTERN = re.compile(r"get_music.php\?key=(.+?)',")

HERE = os.path.dirname(__file__)
TARGET_DIR = os.path.join(HERE, 'download')

client = httpx.AsyncClient(http1=False, http2=True)

async def download_music(url, path):
    # TODO 302 重定向的 Location 取不到真的，被识别出来爬虫
    r = await client.get(url,  follow_redirects=True, headers={
        # 'Accept': '*/*',
        # 'Accept-Encoding': 'identity;q=1, *;q=0',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'bbs_sid=1ue6tkookhh4gro86arohub5ha; Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1699789699; 8f83abd858ac91be10a382e2393459d2=562d9a18f1b7506b26a1abd8bf63ac64; Hm_lpvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1699792840',
        # 'Range': 'bytes=0-',
        # 'Referer': 'https://hifini.com/thread-84250.htm',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        # 'Sec-Fetch-Dest': 'audio',
        # 'Sec-Fetch-Mode': 'no-cors',
        # 'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    })
    print(r.headers)
    if r.status_code == 302:
        print(r.headers['Location'])
        print(r.text)
    if r.status_code >= 200 and r.status_code <= 299:
        d = r.read()
        t = os.path.join(TARGET_DIR, path)
        print(f'download: {url} => {t}')
        td = os.path.dirname(td)
        if not os.path.isdir(td):
            os.makedirs(td)
        with open(t, 'w') as writer:
            writer.write(d)


async def main():
    n = '84250'
    r = httpx.get(f'https://hifini.com/thread-{n}.htm')
    if r.status_code >= 200 and r.status_code <= 299:
        soup = BeautifulSoup(r.text, features='html.parser')
        scripts = soup.find_all('script')
        for script in scripts:
            m = MUSIC_KEY_PATTERN.findall(script.text)
            if len(m) > 0:
                tm = TITLE_PATTERN.findall(script.text)
                title = tm[0] if len(tm) > 0 else n
                am = AUTHOR_PATTERN.findall(script.text)
                author = am[0] if len(am) > 0 else n
                k = m[0]
                u = f"https://hifini.com/get_music.php?key={k}"
                print(f'pick: {title} @ {author} | {u}')
                await download_music(u, f"{title}-{author}.m4a")
    print('main end')


if '__main__' == __name__:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass