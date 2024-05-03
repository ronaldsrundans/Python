from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad

def CBCe():
 print("CBCe")
 f = open("input.txt", "r")
 inputtext=(f.read())
 print("Plain text: ", inputtext)
 data = inputtext.encode('ASCII')
 f.close() 
 cipher = AES.new(key, AES.MODE_CBC)
 ct_bytes = cipher.encrypt(pad(data, AES.block_size))
 iv = b64encode(cipher.iv).decode('utf-8')
 ct = b64encode(ct_bytes).decode('utf-8')
 print("Cypher text: ",ct)
 f = open("iv.txt", "w")
 f.write(iv)
 f.close()
 f = open("ct.txt", "w")
 f.write(ct)
 f.close()
 f = open("output.txt", "w")
 f.write(ct)
 f.close()
 
def CBCd():
 print("CBCd")
 f = open("iv.txt", "r")
 iv=(f.read())
 f.close()
 #f = open("ct.txt", "r")
 f = open("input.txt", "r")
 ct=(f.read())
 f.close()
 iv=b64decode(iv)
 ct = b64decode(ct)
 try: 
  cipher = AES.new(key, AES.MODE_CBC, iv)
  pt = unpad(cipher.decrypt(ct), AES.block_size)
  print("The message was: ", pt)
  f = open("output.txt", "w")
  f.write(pt)
  f.close()
 except (ValueError, KeyError):
  print("Incorrect decryption")
  
def CFBe():
 print("CFBe")
 f = open("input.txt", "r")
 inputtext=(f.read())
 print(inputtext)
 data = inputtext.encode('ASCII')
 f.close()
 cipher = AES.new(key, AES.MODE_CFB)
 ct_bytes = cipher.encrypt(data)
 iv = b64encode(cipher.iv).decode('utf-8')
 ct = b64encode(ct_bytes).decode('utf-8')
 print("Cypher text: ",ct)
 f = open("iv.txt", "w")
 f.write(iv)
 f.close()
 f = open("ct.txt", "w")
 f.write(ct)
 f.close()

def CFBd():
 print("CFBd")
 f = open("iv.txt", "r")
 iv=(f.read())
 f.close()
 #f = open("ct.txt", "r")
 f = open("input.txt", "r")
 ct=(f.read())
 f.close()
 try:
  iv=b64decode(iv)
  ct = b64decode(ct)
  cipher = AES.new(key, AES.MODE_CFB, iv=iv)
  pt = cipher.decrypt(ct)
  print("The message was: ", pt)
  f = open("output.txt", "w")
  f.write(pt)
  f.close()
 except (ValueError, KeyError):
  print("Incorrect decryption")  
  
  

f = open("key.txt", "r")
key=(f.read())#.encode
f.close()
print("key=",key)
key=key.encode('ASCII')


f = open("mac.txt", "r")
mac=(f.read())#.encode
print("mac=", mac)
f.close()

print('Chaining mode number: 1=CBC or 2=CFB')
chainingmode = input()
print('Choose a number: 3-encrypt or 4=decrypt')
crytionmode = input()
print("Your choise is:")
if(chainingmode == '1'):
 print("CBC")
 if(crytionmode == '3'):
  print("encrypt")
  CBCe()
 if(crytionmode == '4'):
  print("decrypt")
  CBCd()  
if(chainingmode == '2'):
 print("CFB")
 if(crytionmode == '3'):
  print("encrypt")
  CFBe()
 if(crytionmode == '4'):
  print("decrypt")
  CFBd()

#MAC
f = open("mac.txt", "w")
f.write("MAC value")
#print(f.read())
f.close()

