import hashlib
import json
from urllib.request import urlopen
from urllib.parse import urlencode


class PickException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class Picker:
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def pick_district(self):
        url = self.make_url('/ws/district/v1/list')
        content = urlopen(url).read()
        data = json.loads(content)
        if data['status'] == 0 and 'result' in data:
            return data['result']
        raise PickException(content)

    def pick_district_children(self, did):
        url = self.make_url('/ws/district/v1/getchildren', id=did)
        content = urlopen(url).read()
        data = json.loads(content)
        if data['status'] == 0 and 'result' in data:
            return data['result']
        raise PickException(content)

    def pick_district_as_tree(self):
        district = self.pick_district()
        for d1 in district[0]:
            if 'cidx' in d1:
                id2 = d1['cidx']
                lv2 = district[1][id2[0]: id2[1] + 1]
                for d2 in lv2:
                    if 'cidx' in d2:
                        id3 = d2['cidx']
                        lv3 = district[2][id3[0]:id3[1] + 1]
                        d2['children'] = lv3
                d1['children'] = lv2
        return district[0]

    def pick_district_as_tree_save_json(self, path):
        tree = self.pick_district_as_tree()
        with open(path, 'w+', encoding='utf-8') as w:
            t = json.dumps(tree, ensure_ascii=False, indent=4)
            w.write(t)

    def make_url(self, path, **param):
        param['key'] = self.key
        query = urlencode(param)
        text = '{}?{}{}'.format(path, query, self.secret)
        m = hashlib.md5()
        m.update(text.encode(encoding='utf-8'))
        sign = m.hexdigest()
        return 'https://apis.map.qq.com{}?{}&sig={}'.format(path, query, sign)
