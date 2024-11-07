import hashlib

def hash_MD5(data):
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()

data = 'Hello, World!'
print('MD5 Hash:', hash_MD5(data))
