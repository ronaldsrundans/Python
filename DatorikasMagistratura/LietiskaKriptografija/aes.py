from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad
#global iv
#global ct
#def CBCe(data, key, iv, ct):
def CBCe(arr):
 print("CBCe")
 data=arr[0]
 key=arr[1]
 iv=arr[2]
 ct=arr[3]
 cipher = AES.new(key, AES.MODE_CBC)
 ct_bytes = cipher.encrypt(pad(data, AES.block_size))
 iv = b64encode(cipher.iv).decode('utf-8')
 ct = b64encode(ct_bytes).decode('utf-8')
 #result = json.dumps({'iv':iv, 'ciphertext':ct})
 #print(result)
 print("cyphertext=",ct)
 arr[2]=iv
 arr[3]=ct

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
#global iv
#global ct
iv=""
ct=""
arr=[]
#print("key=", len(key))

#Encryption
#CBCe(data, key, iv, ct)
arr.append(data)
arr.append(key)
arr.append(iv)
arr.append(ct)
CBCe(arr)
iv=arr[2]
ct=arr[3]
print("iv=",iv)
print("ct=",ct)
#Decryption

# We assume that the key was securely shared beforehand

try:
    #print(iv)
    iv=b64decode(iv)
    ct = b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)

    print("The plain text: ", pt)

except (ValueError, KeyError):

    print("Error! Incorrect decryption")


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

