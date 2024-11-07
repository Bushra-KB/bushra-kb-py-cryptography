from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def generate_ECC_keys():
    private_key = ECC.generate(curve='P-256')
    public_key = private_key.public_key()
    return private_key, public_key

def sign_ECC(private_key, data):
    h = SHA256.new(data.encode('utf-8'))
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(h)
    return signature

def verify_ECC(public_key, data, signature):
    h = SHA256.new(data.encode('utf-8'))
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(h, signature)
        return True
    except ValueError:
        return False

private_key, public_key = generate_ECC_keys()
data = 'Hello, World!'
signature = sign_ECC(private_key, data)
print('Signature:', signature)
print('Verification:', verify_ECC(public_key, data, signature))
