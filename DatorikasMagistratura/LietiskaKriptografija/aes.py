
import json
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad

def CBCe(data, key):
 print("CBCe")
 cipher = AES.new(key, AES.MODE_CBC)
 ct_bytes = cipher.encrypt(pad(data, AES.block_size))
 iv = b64encode(cipher.iv).decode('utf-8')
 ct = b64encode(ct_bytes).decode('utf-8')
 result = json.dumps({'iv':iv, 'ciphertext':ct})
 print(result)

def CBCd(data, key):
 print("CBCe")
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
 
def CFBe(data, key):
 print("CFBe")
 cipher = AES.new(key, AES.MODE_CFB)
 ct_bytes = cipher.encrypt(data)
 iv = b64encode(cipher.iv).decode('utf-8')
 ct = b64encode(ct_bytes).decode('utf-8')
 result = json.dumps({'iv':iv, 'ciphertext':ct})
 print(result)

def CFBd(data, key):
 print("CFBd")
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
#my_function()

def main():
 print("Main function")
 

#print('Enter your plaintext:')
#message = input()
#print('Hello, ' + x)
f = open("plain.txt", "r")
message=(f.read())
print("Plain text is: ",message) 
f.close()
""" 
x='10'
y='01'
while(x!='0' or y!='0'):
 print("Enter the mode number:") 
 print("1=CBC or 2=CFB  or 0=Exit")
 x=input()
 print("Enter number to encrypt or decypt:") 
 print("3=encrypt or 4=decrypt or 0=Exit")
 y=input()
 """
#while(x!='0'):
# x = input()
 
#message="secret"

data = message.encode('ASCII')
print("The message is: ",data)
key = get_random_bytes(16)
print("key=", key)
CBCe(data, key)
CBCd()
#CBCd(...)

#CFB mode
#CFBe(...)


#Decryption 
#CFBd(...)
# We assume that the key was securely shared beforehand


#CMAC
#generate
from cryptography.hazmat.primitives import cmac

from cryptography.hazmat.primitives.ciphers import algorithms

c = cmac.CMAC(algorithms.AES(key))

#c.update(b"message to authenticate")
c.update(data)

c.finalize()

#CMAC
#validate
c = cmac.CMAC(algorithms.AES(key))

#c.update(b"message to authenticate")
c.update(data)

#c.verify(data)

#c.verify(b"an incorrect signature")
#c.verify(b"message to authenticate")
