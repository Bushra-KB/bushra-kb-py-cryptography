import hashlib

def hash_SHA(data):
    sha = hashlib.sha1()
    sha.update(data.encode('utf-8'))
    return sha.hexdigest()

data = 'Hello, World!'
print('SHA-1 Hash:', hash_SHA(data))
