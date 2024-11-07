from Crypto.Cipher import IDEA
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_IDEA(key, data):
    idea = IDEA.new(key, IDEA.MODE_ECB)
    padded_data = pad(data)
    encrypted_data = idea.encrypt(padded_data.encode('utf-8'))
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_IDEA(key, data):
    idea = IDEA.new(key, IDEA.MODE_ECB)
    encrypted_data = base64.b64decode(data)
    decrypted_data = idea.decrypt(encrypted_data).decode('utf-8')
    return decrypted_data.strip()

key = b'Sixteen byte key'
data = 'Hello, World!'
encrypted = encrypt_IDEA(key, data)
print('Encrypted:', encrypted)
print('Decrypted:', decrypt_IDEA(key, encrypted))

