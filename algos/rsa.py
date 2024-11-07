from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_RSA_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_RSA(public_key, data):
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted_data = cipher_rsa.encrypt(data.encode('utf-8'))
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_RSA(private_key, data):
    private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    encrypted_data = base64.b64decode(data)
    decrypted_data = cipher_rsa.decrypt(encrypted_data)
    return decrypted_data.decode('utf-8')

private_key, public_key = generate_RSA_keys()
data = 'Hello, World!'
encrypted = encrypt_RSA(public_key, data)
print('Encrypted:', encrypted)
print('Decrypted:', decrypt_RSA(private_key, encrypted))
