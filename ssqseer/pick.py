import httpx
from bs4 import BeautifulSoup

def let_url(index):
    index_tag = f'_{index}' if index > 1 else ''
    return f'https://www.ssqzj.com/kaijiang/ssqmingxi{index_tag}.html'

def pick_page(index):
    url = let_url(index)
    r = httpx.get(url)
    print(f'{r.status_code} {r.encoding}')
    r.encoding = 'GB2312'
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title)
    table = soup.find(class_='lishi_list')
    if table is not None:
        rows = table.table.tbody.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            number = columns[0].find_all('span')[1].text# 期号 
            open_at = columns[1].text # 日期
            print(number)
            print(open_at)

            balls = columns[2].find(class_='haoma').find_all('span')
            red_balls = [] # 红球
            blue_ball = None # 蓝球
            for ball in balls:
                classes = ball.get('class')
                if 'hong' in classes:
                    red_balls.append(ball.text)
                if 'lan' in classes:
                    blue_ball = ball.text
            print(red_balls)
            print(blue_ball)

def main():
    for i in range(1, 100):
        pick_page(i)


if '__main__' == __name__:
    main()
