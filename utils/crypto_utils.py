import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

SALT = 'S4n0pS01dier----'


def encrypt(message):
    message = message.encode()
    iv = b'0000000000000000'
    raw = pad(message, 16)
    cipher = AES.new(SALT.encode('utf-8'), AES.MODE_CBC, iv)
    enc = cipher.encrypt(raw)
    return base64.b64encode(enc).decode('utf-8')


def decrypt(enc):
    enc = base64.b64decode(enc)
    iv = b'0000000000000000'
    cipher = AES.new(SALT.encode('utf-8'), AES.MODE_CBC, iv)
    dec = cipher.decrypt(enc)
    return unpad(dec, 16).decode('utf-8')
