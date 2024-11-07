from Crypto.Cipher import DES3
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_3DES(key, data):
    des3 = DES3.new(key, DES3.MODE_ECB)
    padded_data = pad(data)
    encrypted_data = des3.encrypt(padded_data.encode('utf-8'))
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_3DES(key, data):
    des3 = DES3.new(key, DES3.MODE_ECB)
    encrypted_data = base64.b64decode(data)
    decrypted_data = des3.decrypt(encrypted_data).decode('utf-8')
    return decrypted_data.strip()

key = DES3.adjust_key_parity(b'Sixteen byte key')
data = 'Hello, World!'
encrypted = encrypt_3DES(key, data)
print('Encrypted:', encrypted)
print('Decrypted:', decrypt_3DES(key, encrypted))
