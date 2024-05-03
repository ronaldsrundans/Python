from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad



#open and read the file after the appending:
f = open("input.txt", "r")
inputtext=(f.read())
print(inputtext)
data = inputtext.encode('ASCII')
#arr=(f.read())
f.close()
f = open("key.txt", "r")
#print(f.read())
key=(f.read())#.encode
f.close()
print("key=",key)
key=key.encode('ASCII')

#print("key=", len(key))


cipher = AES.new(key, AES.MODE_CBC)

ct_bytes = cipher.encrypt(pad(data, AES.block_size))
print("cipher=",ct_bytes)
iv = b64encode(cipher.iv).decode('utf-8')
print("iv=",iv)
ct = b64encode(ct_bytes).decode('utf-8')
print("cyphertext=",ct)
#Decryption

# We assume that the key was securely shared beforehand

try:
    print(iv)
    iv=b64decode(iv)
    ct = b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)

    print("The message was: ", pt)

except (ValueError, KeyError):

    print("Incorrect decryption")


f = open("mac.txt", "r")
#print(f.read())
mac=(f.read())#.encode
print("mac=", mac)
f.close()

print('Chaining mode number: 1-CBC or 2=CFB')
chainingmode = input()
print('Choose a number: 3-encrypt or 4=decrypt')
crytionmode = input()
print("Your choise is:")
if(chainingmode == '1'):
 print("CBC")
 if(crytionmode == '3'):
  print("encrypt")
 if(crytionmode == '4'):
  print("decrypt")  
if(chainingmode == '2'):
 print("CFB")
 if(crytionmode == '3'):
  print("encrypt")
 if(crytionmode == '4'):
  print("decrypt")




f = open("output.txt", "w")
f.write("Now the file has more content!")
#print(f.read())
f.close()
#MAC
f = open("mac.txt", "w")
f.write("MAC value")
#print(f.read())
f.close()

