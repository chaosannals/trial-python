import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

request = urllib.request.Request('https://www.ip.cn', None, {
    ':authority': 'www.ip.cn',
    ':method' : 'GET',
    ':path': '/',
    ':scheme': 'https',
})
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
soup = BeautifulSoup(content, 'html.parser')
