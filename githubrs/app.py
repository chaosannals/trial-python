from genericpath import isdir
import os
import re
from chardet import detect
import httpx
from urllib.parse import urlparse
from subprocess import check_output, CalledProcessError
from loguru import logger
from bs4 import BeautifulSoup
from conf import CONF


def run(cmd):
    '''

    '''

    try:
        out_bytes = check_output(cmd)
    except CalledProcessError as e:
        out_bytes = e.output

    # TODO encoding = None
    cd = detect(out_bytes)
    return out_bytes.decode(cd['encoding'])


class GitHubClient:
    '''

    '''

    def __init__(self, user, proxies=None, target=None):
        '''

        '''

        self.user = user
        self.proxies = proxies
        self.target = target if target is not None else os.path.realpath(
            __file__)
        self.pull_success = []
        self.pull_fail = []
        self.clone_success = []
        self.clone_fail = []

    def get_repositories_link(self, page=1):
        '''

        '''

        result = []
        with httpx.Client(proxies=self.proxies) as client:
            r = client.get(
                f'https://github.com/{self.user}?page={page}&tab=repositories')
            soup = BeautifulSoup(r.read(), features='html.parser')
            lis = soup.find_all('li', {'class': ['public', 'source']})
            for li in lis:
                lias = li.find_all('a')
                for lia in lias:
                    c = lia.get('class')
                    if c is None:
                        result.append(lia.get('href'))
                    elif 'Link--muted' in c:
                        pass
                        # print(lia.get('href'))
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

    def pull_project(self, pn: str, pd: str):
        '''

        '''

        info = {
            'project': pn,
            'directory': pd,
        }
        os.chdir(pd)
        r = run(['git', 'pull'])
        logger.info(r)
        if r.find('Already up to date') >= 0:
            self.pull_success.append(info)
        else:
            self.pull_fail.append(info)

    def clone_project(self, td: str, pn: str, go: str):
        '''

        '''

        info = {
            'target': td,
            'project': pn,
            'origin': go,
        }

        if not os.path.isdir(td):
            os.makedirs(td)
        os.chdir(td)
        r = run(['git', 'clone', go])
        logger.info(r)
        self.clone_success.append(info)


@logger.catch
def main():
    '''

    '''

    ghc = GitHubClient(**CONF)
    infos = ghc.get_repositories_info_all()
    for info in infos:
        pd = info['project_dir']
        pn = info['project']
        if os.path.isdir(pd):
            pg = os.path.join(pd, '.git')
            if os.path.isdir(pg):
                logger.info(
                    f'[{pn}]------------------------------------------------[start]')
                ghc.pull_project(pn, pd)
                logger.info(
                    f'[{pn}]------------------------------------------------[end]')
                continue
        # 克隆
        logger.info(
            f'<clone>[{pn}]------------------------------------------------[start]')
        td = info['target_dir']
        go = info['git_origin']
        ghc.clone_project(td, pn, go)
        logger.info(
            f'<clone>[{pn}]------------------------------------------------[end]')

    logger.warning('pull fail')
    for pf in ghc.pull_fail:
        logger.warning(pf)

    input('按回车结束')


if '__main__' == __name__:
    main()
