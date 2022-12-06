SSH_HOST = '127.0.0.1'
SSH_USER = 'youraccount'
SSH_PASS = '1234567'
SSH_ROOT_PASS = '132456789'
SSH_CMDS = [
    'su',
    SSH_ROOT_PASS,
    'cd /a/path/gitrep',
    'git branch -avv',
    'git pull',
    'git branch -avv',
    'git status',
]