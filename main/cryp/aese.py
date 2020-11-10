from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# pip install pycryptodome

data = b'aaaaaaabbbbbbb'
key = b'1234567890qwerty'
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("temp/encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()