
#https://www.comparitech.com/blog/information-security/md5-algorithm-with-examples/
def string2bin(plaintext):
	#print()
	res = ''.join(format(ord(i), '08b') for i in plain_text)
	return res


def bin2string(binres):
	str = ""
	for i in range(0, len(binres), 8):
		binc = binres[i:i + 8]
		num = int(binc, 2)
		str += chr(num)
	return str
def num2bin(num):
	x=bin(num)[2:]
	return x
def hex2bin(hex_num):#Takes only 2 letters/numbers like "ff" or "00" LOWERCASE!!!
	hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
	binary = ''
	for digit in hex_num:
		binary += hex_dict[digit]
	binary=list(binary)
	#print(binary)
	return binary
def fullHex2Bin(b,arr):
	for i in range(4):
		tmp=[]
		tmp=hex2bin(b[0+i*2:2+i*2].lower())
		for j in range(8):
			arr.append(tmp[j])
	print(arr)

def bin2hex(n):
    # convert binary to int
    num = int(n, 2)
    # convert int to hexadecimal
    hex_num = format(num, 'x')
    return(hex_num)
def ANDfunction(x,y):
	if(x==y):
		return '1'
	else:
		return '0'
def ORfunction(x,y):
	if(x!=y):
		return '1'
	else:
		return '0'
def NOTfunction(x):
	if(x==1):
		return '0'
	else:
		return '1'
def ffunction(B,C,D):
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
def hexCheck(arr):
	for i in range(8):
		print(bin2hex((arr[i*4])+(arr[i*4+1])+(arr[i*4+2])+(arr[i*4+3])))

def modSum(a,b):
	c=[]
	#print("modSum a", a)
	#print("modSum b", b)
	for i in range(32):
		c.append('0')
	for i in range(31,-1,-1):
		x=((int(a[i])+int(b[i])+int(c[i])))
		c[i]=(x%2)
		if((i>0)and(x>1)):
		    c[i-1]=1
	
	return c
def leftBitShift(arr,n):
	#print(arr)
	tmp=[]
	for i in range(n):
		tmp.append(arr[i])
	for i in range(n):
		arr.pop(0)
		arr.append(tmp[i])
	#print("tmp=", tmp)
	#print(arr)
    #return 0
def endShuffle(A,B,C,D,E):
	for i in range (32):
		A[i]=D[i]
		D[i]=C[i]
		C[i]=B[i]
		B[i]=E[i]
    #B=arr_mSB
    #C=B
    #D=C
	#return 0
#plain_text="KINO"
plain_text="They are deterministic"
print("The message is : " + str(plain_text))
res=string2bin(plain_text) 
# printing result 
print("The string after binary conversion : " + str(res))
#1. Append Padding Bits:
l_res=len(res) 
print("Lenght of message:",l_res)
res=res+'1'
for x in range(l_res,511-64):
	#print(x) 
	res=res+'0'
print("Padded 0-os lenght",len(res))	
l_bin=num2bin(l_res)
print("l_bin", l_bin)
l_bin2=len(l_bin)
print("l_bin2", l_bin2)
for y in range(l_bin2, 64):
	#print(y)
	res=res+'0'
res=res+l_bin

print(len(res))	#M

print("The binary value is:", res)
  
# print binary data
str=bin2string(res)
print("Plain text: ", str)

A_bin=[]
B_bin=[]
C_bin=[]
D_bin=[]
fullHex2Bin("01234567", A_bin)
fullHex2Bin("89abcdef", B_bin)
fullHex2Bin("fedcba98", C_bin)
fullHex2Bin("76543210", D_bin)





#M 2D masīvs 
"""
rows, cols = (16, 32)
arr = [[0]*cols]*rows
for i in range(16):
	for j in range(32):
		#print(i,j)
		arr[i][j]=res[i*32+j]
"""


arr_F=(ffunction(B_bin, C_bin, D_bin))#(89abcdef,fe dc ba 98, 76 54 32 10)
arr_mS=(modSum(A_bin,arr_F))# ffffffff

M_bin=[]
fullHex2Bin("54686579", M_bin)
arr_mS0=(modSum(M_bin,arr_mS))# 54686578

K_bin=[]#K value
#(hex2bin("d7")+hex2bin("6a")+hex2bin("a4")+hex2bin("78"))
#          word  K1 – D76AA478
fullHex2Bin("d76aa478", K_bin)

arr_mK1=(modSum(K_bin,arr_mS0))# 2bd309f0

leftBitShift(arr_mK1,7) #e984f815

arr_mSB=(modSum(B_bin,arr_mK1))# 7330C604



endShuffle(A_bin,B_bin,C_bin,D_bin,arr_mSB)
num=[]
for i in range(32):
    num.append( "{}".format(A_bin[i]))
print("A=")
hexCheck(num)
num=[]
for i in range(32):
    num.append( "{}".format(B_bin[i]))
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

### end of 1 operation 63 more operations
"""
be = "01234567"
#"01234567"
bearr=[]
fullHex2Bin(be, bearr)
print("be=", bearr)
num=[]
for i in range(32):
    num.append( "{}".format(bearr[i]))
print("Bear=")
hexCheck(num)
"""

"""




    M0 – 54686579
    M1 – 20617265
    M2 – 20646574
    M3 – 65726D69
    M4 – 6E697374
    M5 – 69638000
    M6 – 00000000
    M7 – 00000000
    M8 – 00000000
    M9 – 00000000
    M10 – 00000000
    M11 – 00000000
    M12 – 00000000
    M13 – 00000000
    M14 – 00000000
    M15 – 000000B0

m0=[]
for i in range(32):
	m0.append(arr[0][i])
arr_MS=(modSum(arr_mS,m0))
print(arr_MS)


"""

#second : M1, M6, M11, M0, M5, M10, M15, M4, M9, M14, M3, M8, M13, M2, M7, M12
#third : M5, M8, M11, M14, M1, M4, M7, M10, M13, M0, M3, M6, M9, M12, M15, M2
#forth : M0, M7, M14, M5, M12, M3, M10, M1, M8, M15, M6, M13, M4, M11, M2, M9
#for i in range(32):
#	print(arr[i])
"""

    K1 – D76AA478
    K2 – E8C7B756
    K3 – 242070DB
    K4 – C1BDCEEE
    K5 – F57COFA
    K6 – 4787C62A
    K7 – A8304613
    K8 – FD469501
    K9 – 698098D8
    K10 – 8B44F7AF
    K11 – FFFF5BB1
    K12 – 895CD7BE
    K13 – 6B901122
    K14 – FD987193
    K15 – A679438E
    K16 – 49B40821
    K17 – F61E2562
    K18 – C040B340
    K19 – 265E5A51
    K20 – E9B6C7AA
    K21 – D62F105D
    K22 – 02441453
    K23 – D8A1E681
    K24 – E7D3FBC8
    K25 – 21E1CDE6
    K26 – C33707D6
    K27 – F4D50D87
    K28 – 455A14ED
    K29 – A9E3E905
    K30 – FCEFA3F8
    K31 – 676F02D9
    K32 – 8D2A4C8A
    K33 – FFFA3942
    K34 – 8771F681
    K35 – 699D6122
    K36 – FDE5380C
    K37– A4BEEA44
    K38 – 4BDECFA9
    K39 – F6BB4B60
    K40 – BEBFBC70
    K41 – 289B7EC6
    K42 – EAA127FA
    K43 – D4EF3085
    K44 – 04881D05
    K45 – D9D4D039
    K46 – E6DB99E5
    K47 – 1FA27CF8
    K48 – C4AC5665
    K49 – F4292244
    K50 – 432AFF97
    K51 – AB9423A7
    K52 – FC93A039
    K53 – 655B59C3
    K54 – 8F0CCC92
    K55 – FFEFF47D
    K56 – 85845DD1
    K57 – 6FA87E4F
    K58 – FE2CE6E0
    K59 – A3014314
    K60 – 4E0811A1
    K61 – F7537E82
    K62 – BD3AF235
    K63 – 2AD7D2BB
    K64 – EB86D391

    Round one
        S1, S5, S9, S13 – 7
        S2, S6, S10, S14 – 12
        S3, S7, S11, S15 – 17
        S4, S8, S12, S16, – 22

    Round two
        S17, S21, S25, S29 – 5
        S18, S22, S26, S30 – 9
        S19, S23, S27, S31 – 14
        S20, S24, S28, S32 – 20

    Round three
        S33, S37, S41, S45 – 4
        S34, S38, S42, S46 – 11
        S35, S39, S43, S47 – 16
        S36, S40, S44, S48 – 13

    Round four
        S49, S53, S57, S61 – 6
        S50, S54, S58, S62 – 10
        S51, S55, S59, S63 – 15
        S52, S56, S60, S64 – 21

rows, cols = (32, 16)
# method 2 1st approach
arr = [[0]*cols]*rows
for i in range(32):
	arr[0][i]=1
	print(i)
"""
