from Crypto.Hash import CMAC
from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad
from Crypto.Hash import CMAC


#secret = "2b7e151628aed2a6abf7158809cf4f3c"
secret = b'Sixteen byte key'
#msg = "6bc1bee22e409f96e93d7e117393172a"
msg =b'Sixteen byte key'
cobj = CMAC.new(bytes(secret), ciphermod=AES)
cobj.update(bytes(msg))
res = cobj.hexdigest()
print(res)




cobj = CMAC.new(bytes(secret), ciphermod=AES)
cobj.update(bytes(msg))
#res = cobj.hexdigest()
print(bytes.fromhex(res))
try:

  cobj.verify(bytes.fromhex(res))

  print ("The message '%s' is authentic")# % msg

except ValueError:

  print ("The message or the key is wrong")
