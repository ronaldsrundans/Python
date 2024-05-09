from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad
from Crypto.Hash import CMAC
def MACfunction(ct_bytes):
 cobj = CMAC.new(key, ciphermod=AES)
 cobj.update(bytes(ct_bytes))
 res = cobj.hexdigest() 
 print("MAC: ",res)
 f = open("mac.txt", "w")
 f.write(res)
 f.close()
 return res
def CBCe():
 print("Function CBCe")
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

 """
 cobj = CMAC.new(key, ciphermod=AES)
 cobj.update(bytes(ct_bytes))
 res = cobj.hexdigest() 
 print("MAC: ",res)
 """
 MACfunction(ct_bytes)
 
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
 print("Function CBCd")
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
  f.write(str(pt))
  #f.write(b64decode(pt))
  f.close()
  MACfunction(ct)
  """
  cobj = CMAC.new(key, ciphermod=AES)
  cobj.update(bytes(ct))
  #cobj.update(bytes(msg))
  res = cobj.hexdigest() 
  print("MAC: ",res)
  """
 except (ValueError, KeyError):
  print("Incorrect decryption")
  
def CFBe():
 print("Function CFBe")
 f = open("input.txt", "r")
 inputtext=(f.read())
 print("Plain text: ", inputtext)
 data = inputtext.encode('ASCII')
 f.close()
 cipher = AES.new(key, AES.MODE_CFB)
 ct_bytes = cipher.encrypt(data)
 iv = b64encode(cipher.iv).decode('utf-8')
 ct = b64encode(ct_bytes).decode('utf-8')
 print("Cypher text: ",ct)
 
 ct_bytes = cipher.encrypt(pad(data, AES.block_size))
 cobj = CMAC.new(key, ciphermod=AES)
 cobj.update(bytes(ct_bytes))
 res = cobj.hexdigest() 
 print("MAC: ",res)
 
 f = open("iv.txt", "w")
 f.write(iv)
 f.close()
 f = open("ct.txt", "w")
 f.write(ct)
 f.close()
 f = open("output.txt", "w")
 f.write(ct)
 f.close()


def CFBd():
 print("Function CFBd")
 f = open("iv.txt", "r")
 iv=(f.read())
 f.close()
 #f = open("ct.txt", "r")
 f = open("input.txt", "r")
 ct=(f.read())
 f.close()
 print("ct1=",ct)
 try:
  iv=b64decode(iv)
  ct = b64decode(ct)
  print("ct2=",ct)
  cipher = AES.new(key, AES.MODE_CFB, iv=iv)
  pt = cipher.decrypt(ct)
  print("The message was: ", pt)
  f = open("output.txt", "w")
  f.write(str(pt))
  f.close()
  #MAC value generate
  data = pt
  cipher = AES.new(key, AES.MODE_CFB)
  ct_bytes = cipher.encrypt(pad(data, AES.block_size))
  cobj = CMAC.new(key, ciphermod=AES)
  cobj.update(bytes(ct_bytes))
  res = cobj.hexdigest() 
  print("MAC: ",res)
  #END MAC value generate
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

