
def string2bin(plaintext): #string to binary
	#print()
	res = ''.join(format(ord(i), '08b') for i in plain_text)
	return res
def bin2string(binres): #binary to string
	str = ""
	for i in range(0, len(binres), 8):
		binc = binres[i:i + 8]
		num = int(binc, 2)
		str += chr(num)
	return str
def num2bin(num):#dec to bin
	x=bin(num)[2:]
	return x
def hex2bin(hex_num):#Takes only 2 letters/numbers like "ff" or "00" LOWERCASE!!!
	hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
	binary = ''
	for digit in hex_num:
		binary += hex_dict[digit]
	binary=list(binary)
	return binary
def fullHex2Bin(b,arr): # convert binary arr (len 32)to Hex  
	for i in range(4):
		tmp=[]
		tmp=hex2bin(b[0+i*2:2+i*2].lower())
		for j in range(8):
			arr.append(tmp[j])
def bin2hex(n):   
    num = int(n, 2) # convert binary to int    
    hex_num = format(num, 'x')# convert int to hexadecimal
    return(hex_num)
def ANDfunction(x,y):	
	if(int(x)&int(y)):
		return '1'
	else:
		return '0'
def ORfunction(x,y):	
	if(int(x)|int(y)):
		return '1'
	else:
		return '0'
def NOTfunction(x):
	if(x=='1'):
		return '0'
	else:
		return '1'
def XORfunction(x,y):
	if(int('0')^int('0')):
		return '1'
	else:
		return '0'
def ffunction(B,C,D):#F  (B AND C) OR (NOT B AND D)
	arr=[]
	arr2=[]
	arr3=[]
	arr4=[]
	for i in range(32):
		arr.append(ANDfunction(B[i],C[i]))
	for i in range(32):
		arr2.append(NOTfunction(B[i]))
	for i in range(32):
		arr3.append(ANDfunction(arr2[i],D[i]))
	for i in range(32):
		arr4.append(ORfunction(arr[i],arr3[i]))
	return arr4
def gfunction(B,C,D):	#(B AND D)OR(C AND NOT(D))
	arr=[]
	arr2=[]
	arr3=[]
	arr4=[]
	for i in range(32):
		arr.append(ANDfunction(B[i],D[i]))
	for i in range(32):
		arr2.append(NOTfunction(D[i]))
	for i in range(32):
		arr3.append(ANDfunction(C[i],arr2[i]))
	for i in range(32):
		arr4.append(ORfunction(arr[i],arr3[i]))
	return arr4
def hfunction(B,C,D):	#(B XOR C XOR D)
	arr=[]
	arr3=[]
	for i in range(32):
		arr.append(XORfunction(B[i],C[i]))
	for i in range(32):
		arr3.append(XORfunction(arr[i],D[i]))
	return arr3

def ifunction(B,C,D): #“C OR, BUT NOT BOTH (B OR NOT-D)
	arr=[]
	arr2=[]
	arr3=[]
	for i in range(32):
		arr.append(NOTfunction(D[i]))
	for i in range(32):
		arr2.append(ORfunction(B[i],arr[i]))
	for i in range(32):
		arr3.append(XORfunction(C[i],arr2[i]))
	return arr3
def hexCheck(arr):#len(arr) must be 32bits (bin form) => 2 hex values 
	for i in range(8):#4*8=32
		print(bin2hex((arr[i*4])+(arr[i*4+1])+(arr[i*4+2])+(arr[i*4+3])))
def modSum(a,b):# Modular addition
	c=[]
	for i in range(32):
		c.append('0')
	for i in range(31,-1,-1):
		x=((int(a[i])+int(b[i])+int(c[i])))
		c[i]=(x%2)
		if((i>0)and(x>1)):
		    c[i-1]=1
	return c
def leftBitShift(arr,n):#shift n first bits to end of arr
	tmp=[]
	for i in range(n):
		tmp.append(arr[i])
	for i in range(n):
		arr.pop(0)
		arr.append(tmp[i])
def endShuffle(A,B,C,D,E):#After each round switch values
	for i in range (32):
		A[i]=D[i]
		D[i]=C[i]
		C[i]=B[i]
		B[i]=E[i]
def printVectors(A,B,C,D):#print A,B,C,D in Hex
	num=[]
	for i in range(32):
		num.append( "{}".format(A[i]))
	print("A=")
	hexCheck(num)
	num=[]
	for i in range(32):
			num.append( "{}".format(B[i]))
	print("B=")
	hexCheck(num)
	num=[]
	for i in range(32):
		num.append( "{}".format(C_bin[i]))
	print("C=")
	hexCheck(num)
	num=[]
	for i in range(32):
		num.append( "{}".format(D_bin[i]))
	print("D=")
	hexCheck(num)
def printVector(A):#print just A in Hex
	num=[]
	for i in range(32):
		num.append( "{}".format(A[i]))
	print("Vector=")
	hexCheck(num)
def isItPrime (num):#Is this number a prime number?
	for i in range(2,num):
		if (num % i == 0):
			return False
	return True
def gcd(a, h):#Greatest Common Divider
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp		
def encrypt(message, e,n):# To encrypt the given number
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        encrypted_text %= n
        e -= 1
    return encrypted_text
def decrypt(c,d,n):# To decrypt the given number

    decrypted = 1
    while d > 0:
        decrypted *= c
        decrypted %= n
        d -= 1
    return decrypted
#RSA algoritms
p=191#
q=163#
#print(isItPrime(191))
#print(isItPrime(163))
n=p*q #must be >256
e=2	# e*d=1(mod z)# 2 # >1 and not a factor of z
z=(p-1)*(q-1)	
k = 1 #konstante pie d aprēķina
d=0
while (e < z):#meklē atbilstošass e un d
	if(gcd(e, z) == 1):
		for k in range(1,n):
			d = (1 + (k*z))/e 
			if(d%1==0):#d ir vesels skaitlis
				break
		if(d%1==0):
			break
		e = e+1#citādi bezgalīgs cikls
	else:
		e = e+1
print("Public key pair (e,n):") 
print(e,n)
print("Private key pair (d,n):") 
print(d,n)

		
#/RSA algoritms
#MD5 algoritms
plain_text="KINO"
res=string2bin(plain_text) #string after binary conversion : " + str(res))
l_res=len(res) 
res=res+'1'
for x in range(l_res,511-64):#1. Append Padding Bits:
	res=res+'0'
l_bin=num2bin(l_res)
l_bin2=len(l_bin)
for y in range(l_bin2, 64):
	res=res+'0'
res=res+l_bin
str=bin2string(res)
print("Plain text: ", plain_text)
res=list(res)
Karr=["D76AA478","E8C7B756","242070DB","C1BDCEEE","f57c0faf","4787C62A","A8304613","FD469501","698098D8","8B44F7AF","FFFF5BB1","895CD7BE","6B901122","FD987193","A679438E","49B40821","F61E2562","C040B340","265E5A51","E9B6C7AA","D62F105D","02441453","D8A1E681","E7D3FBC8","21E1CDE6","C33707D6","F4D50D87","455A14ED","A9E3E905","FCEFA3F8","676F02D9","8D2A4C8A","FFFA3942","8771F681","699D6122","FDE5380C","A4BEEA44","4BDECFA9","F6BB4B60","BEBFBC70","289B7EC6","EAA127FA","D4EF3085","04881D05","D9D4D039","E6DB99E5", "1FA27CF8","C4AC5665","F4292244","432AFF97","AB9423A7","FC93A039","655B59C3","8F0CCC92","FFEFF47D","85845DD1","6FA87E4F","FE2CE6E0","A3014314","4E0811A1","F7537E82","BD3AF235","2AD7D2BB","EB86D391"]
Sarr=[7,12,17,22,7,12,17,22,7,12,17,22,7,12,17,22,5,9,14,20,5,9,14,20,5,9,14,20,5,9,14,20,4,11,16,13,4,11,16,13,4,11,16,13,4,11,16,13,6,10,15,21,6,10,15,21,6,10,15,21,6,10,15,21]
Marr=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,6,11,0,5,10,15,4,9,14,3,8,13,2,7,12,5,8,11,14,1,4,7,10,13,0,3,6,9,12,15,2,0,7,14,5,12,3,10,1,8,15,6,13,4,11,2,9]
M_arr=[]
for i in range(16):
	tmp=[]
	for j in range(32):
		tmp.append(res[i*32+j])
	M_arr.append(tmp)	
A_bin=[]
B_bin=[]
C_bin=[]
D_bin=[]
A_bin0=[]
B_bin0=[]
C_bin0=[]
D_bin0=[]
fullHex2Bin("01234567", A_bin)
fullHex2Bin("89abcdef", B_bin)
fullHex2Bin("fedcba98", C_bin)
fullHex2Bin("76543210", D_bin)
fullHex2Bin("01234567", A_bin0)
fullHex2Bin("89abcdef", B_bin0)
fullHex2Bin("fedcba98", C_bin0)
fullHex2Bin("76543210", D_bin0)
#round 1
for r in range(0,16):
	arr_F=(ffunction(B_bin, C_bin, D_bin))# F function
	arr_mS=(modSum(A_bin,arr_F))# 		#A+F
	arr_mS0=(modSum(M_arr[Marr[r]],arr_mS)) #M value	A+M
	K_bin=[]           
	fullHex2Bin(Karr[r], K_bin) #K value
	arr_mK1=(modSum(K_bin,arr_mS0))# 	M+K
	leftBitShift(arr_mK1,Sarr[r]) #    #S value
	arr_mSB=(modSum(B_bin,arr_mK1))# 	A+S
	endShuffle(A_bin,B_bin,C_bin,D_bin,arr_mSB)
#round 2
for r in range(16,33):
	arr_F=(gfunction(B_bin, C_bin, D_bin))# G function
	arr_mS=(modSum(A_bin,arr_F))# 
	arr_mS0=(modSum(M_arr[Marr[r]],arr_mS))# #M value
	K_bin=[]           
	fullHex2Bin(Karr[r], K_bin) #K value
	arr_mK1=(modSum(K_bin,arr_mS0))# 
	leftBitShift(arr_mK1,Sarr[r]) #    #S value
	arr_mSB=(modSum(B_bin,arr_mK1))# 
	endShuffle(A_bin,B_bin,C_bin,D_bin,arr_mSB)
#round 3
for r in range(33,49):
	arr_F=(hfunction(B_bin, C_bin, D_bin))# H function
	arr_mS=(modSum(A_bin,arr_F))# 
	arr_mS0=(modSum(M_arr[Marr[r]],arr_mS))  #M value
	K_bin=[]           
	fullHex2Bin(Karr[r], K_bin) #K value
	arr_mK1=(modSum(K_bin,arr_mS0))
	leftBitShift(arr_mK1,Sarr[r])     #S value
	arr_mSB=(modSum(B_bin,arr_mK1))
	endShuffle(A_bin,B_bin,C_bin,D_bin,arr_mSB)
#round 4
for r in range(49,64):
	arr_F=(ifunction(B_bin, C_bin, D_bin))# I function
	arr_mS=(modSum(A_bin,arr_F))# 
	arr_mS0=(modSum(M_arr[Marr[r]],arr_mS))#  #M value
	K_bin=[]           
	fullHex2Bin(Karr[r], K_bin) #K value
	arr_mK1=(modSum(K_bin,arr_mS0))# 
	leftBitShift(arr_mK1,Sarr[r]) #    #S value
	arr_mSB=(modSum(B_bin,arr_mK1))#
	endShuffle(A_bin,B_bin,C_bin,D_bin,arr_mSB)
#Last bitwise sum
A_bin=(modSum(A_bin,A_bin0))
B_bin=(modSum(B_bin,B_bin0))
C_bin=(modSum(C_bin,C_bin0))
D_bin=(modSum(D_bin,D_bin0))
#/MD5 algoritms
first_byte=[]#Pirmais bits no MD5
for i in range(8):
	first_byte.append(A_bin[i])
print("First byte=",first_byte)
#RSA algoritms
msg=int(first_byte[7])+2*int(first_byte[6])+4*int(first_byte[5])+8*int(first_byte[4])+16*int(first_byte[3])+32*int(first_byte[2])+64*int(first_byte[1])+128*int(first_byte[0])
print("Message Hash value (dec) = ", msg)
c=encrypt(msg, e,n)
print("Crypted Hash value (dec) = ", c)
print("Signed message = ", plain_text,c)
#print(c)
msg=decrypt(c, d,n)
print("Decrypted Hash value:",msg)
#/RSA algoritms
