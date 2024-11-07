from Crypto.Cipher import DES
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_DES(key, data):
    des = DES.new(key, DES.MODE_ECB)
    padded_data = pad(data)
    encrypted_data = des.encrypt(padded_data.encode('utf-8'))
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_DES(key, data):
    des = DES.new(key, DES.MODE_ECB)
    encrypted_data = base64.b64decode(data)
    decrypted_data = des.decrypt(encrypted_data).decode('utf-8')
    return decrypted_data.strip()

key = b'8bytekey'
data = 'Hello, World!'
encrypted = encrypt_DES(key, data)
print('Encrypted:', encrypted)
print('Decrypted:', decrypt_DES(key, encrypted))
