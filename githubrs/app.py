from genericpath import isdir
import os
import httpx
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from conf import CONF

class GitHubClient:
    '''
    
    '''
    def __init__(self, user, proxies=None, target=None):
        '''
        
        '''
        
        self.user = user
        self.proxies = proxies
        self.target = target if target is not None else os.path.realpath(__file__)

    def get_repositories_link(self, page=1):
        '''
        
        '''
        
        result = []
        with httpx.Client(proxies=self.proxies) as client:
            r = client.get(f'https://github.com/{self.user}?page={page}&tab=repositories')
            soup = BeautifulSoup(r.read(), features='html.parser')
            lis = soup.find_all('li', { 'class': ['public', 'source']})
            for li in lis:
                lias = li.find_all('a')
                for lia in lias:
                    c = lia.get('class')
                    if c is None:
                        result.append(lia.get('href'))
                    elif 'Link--muted' in c:
                        pass
                        #print(lia.get('href'))
        return result

    def get_repositories_link_all(self):
        p = 1
        result = []
        while True:
            r = self.get_repositories_link(p)
            if len(r) == 0:
                break
            result.extend(r)
            p += 1
        return result

    def get_repositories_info_all(self):
        '''
        
        '''
        links = self.get_repositories_link_all()
        result = []
        for link in links:
            url = urlparse(link)
            p = url.path.strip('/')
            pn = p.split('/')[1]
            t = f'git@github.com:{p}.git'
            td = os.path.join(self.target, self.user)
            pd = os.path.join(td, pn)
            r = {
                'user': self.user,
                'link': link,
                'path': p,
                'git_origin': t,
                'target_dir': td,
                'project': pn,
                'project_dir': pd,
            }
            result.append(r)
        return result

if '__main__' == __name__:
    ghc = GitHubClient(**CONF)
    infos = ghc.get_repositories_info_all()
    for info in infos:
        pd = info['project_dir']
        pn = info['project']
        if os.path.isdir(pd):
            pg = os.path.join(pd, '.git')
            if os.path.isdir(pg):
                print(f'[{pn}]------------------------------------------------[start]')
                os.chdir(pd)
                os.system('git pull')
                print(f'[{pn}]------------------------------------------------[end]')
                continue
        # 克隆
        td = info['target_dir']
        go = info['git_origin']
        if not os.path.isdir(td):
            os.makedirs(td)
        print(f'<clone>[{pn}]------------------------------------------------[start]')
        os.chdir(td)
        os.system(f'git clone {go}')
        print(f'<clone>[{pn}]------------------------------------------------[end]')

input('按回车结束')