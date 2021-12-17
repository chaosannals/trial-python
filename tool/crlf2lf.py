import os

SUFFIX_GROUP = [
    'm4',
    'sh',
    'guess',
    'sub',
]

def list_file(folder):
    '''
    列举目录下的文件
    '''

    result = []
    dirname = os.path.realpath(folder)
    for i in os.listdir(dirname):
        path = os.path.realpath(dirname + '/' + i)
        if os.path.isdir(path):
            result.extend(list_file(path))
        else:
            result.append(path)
    return result

def main():
    '''
    
    '''

    fs = list_file('.')
    for f in fs:
        print(f)

if __name__ == '__main__':
    main()