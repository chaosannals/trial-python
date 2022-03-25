import sys


def load_lines(path):
    '''
    读取行
    '''

    lines = set()
    with open(path, 'r', encoding='utf8') as reader:
        for line in reader.readlines():
            content = line.strip()
            if len(content) > 0:
                lines.add(content)
    return lines


def main():
    '''
    找出不同。
    '''

    if len(sys.argv) < 3:
        print('diffline /one/path /two/path')
        return
    p1 = load_lines(sys.argv[1])
    p2 = load_lines(sys.argv[2])
    return p1 ^ p2


if __name__ == '__main__':
    main()
