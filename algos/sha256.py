import hashlib

def hash_SHA256(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

data = 'Hello, World!'
print('SHA-256 Hash:', hash_SHA256(data))
