from Crypto.Cipher import AES
import base64

def encrypt_AES(key, data):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def decrypt_AES(key, data):
    raw_data = base64.b64decode(data)
    nonce = raw_data[:16]
    ciphertext = raw_data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')

key = b'Sixteen byte key'
data = 'Hello, World!'
encrypted = encrypt_AES(key, data)
print('Encrypted:', encrypted)
print('Decrypted:', decrypt_AES(key, encrypted))
