#CBC mode
import json

from base64 import b64encode

from base64 import b64decode

from Crypto.Cipher import AES

from Crypto.Util.Padding import pad

from Crypto.Random import get_random_bytes

from Crypto.Util.Padding import unpad

print('Enter your plaintext:')
message = input()
#print('Hello, ' + x) 
data = message.encode('ASCII')
print("The message is: ",data)
key = get_random_bytes(16)
print("key=", key)
cipher = AES.new(key, AES.MODE_CBC)

ct_bytes = cipher.encrypt(pad(data, AES.block_size))

iv = b64encode(cipher.iv).decode('utf-8')

ct = b64encode(ct_bytes).decode('utf-8')

result = json.dumps({'iv':iv, 'ciphertext':ct})

print(result)

#Decryption

# We assume that the key was securely shared beforehand

try:

    b64 = json.loads(result)

    iv = b64decode(b64['iv'])

    ct = b64decode(b64['ciphertext'])

    cipher = AES.new(key, AES.MODE_CBC, iv)

    pt = unpad(cipher.decrypt(ct), AES.block_size)

    print("The message was: ", pt)

except (ValueError, KeyError):

    print("Incorrect decryption")
#CFB mode

cipher = AES.new(key, AES.MODE_CFB)

ct_bytes = cipher.encrypt(data)

iv = b64encode(cipher.iv).decode('utf-8')

ct = b64encode(ct_bytes).decode('utf-8')

result = json.dumps({'iv':iv, 'ciphertext':ct})

print(result)

#Decryption 

# We assume that the key was securely shared beforehand

try:

    b64 = json.loads(result)

    iv = b64decode(b64['iv'])

    ct = b64decode(b64['ciphertext'])

    cipher = AES.new(key, AES.MODE_CFB, iv=iv)

    pt = cipher.decrypt(ct)

    print("The message was: ", pt)

except (ValueError, KeyError):

    print("Incorrect decryption")

#CMAC
#generate
from cryptography.hazmat.primitives import cmac

from cryptography.hazmat.primitives.ciphers import algorithms

c = cmac.CMAC(algorithms.AES(key))

c.update(b"message to authenticate")

c.finalize()

#CMAC
#validate
c = cmac.CMAC(algorithms.AES(key))

c.update(b"message to authenticate")

#c.verify(b'CT\x1d\xc8\x0e\x15\xbe4e\xdb\xb6\x84\xca\xd9Xk')

#c.verify(b"an incorrect signature")
#c.verify(b"message to authenticate")
