def guess_picture_suffix(body: bytes):
    '''
    通过文件头猜后缀
    '''

    if body.startswith(b'\xff\xd8'):
        return 'jpg'
    if body.startswith(b'\x42\x4d'):
        return 'bmp'
    if body.startswith(b'\x47\x49\46'):
        return 'gif'
    if body.startswith(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'):
        return 'png'
    return None
