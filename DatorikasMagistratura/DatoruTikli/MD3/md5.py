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
def hex2bin(hex_num):
	hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
	binary = ''
	for digit in hex_num:
		binary += hex_dict[digit]
	#print(binary)
	return binary
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

print(len(res))	

print("The binary value is:", res)
  
# print binary data
str=bin2string(res)
print("Plain text: ", str)
#		  word A: 01 23 45 67
A_bin=(hex2bin("01")+hex2bin("23")+hex2bin("45")+hex2bin("67"))
#          word B: 89 ab cd ef
B_bin=(hex2bin("89")+hex2bin("ab")+hex2bin("cd")+hex2bin("ef"))
#          word C: fe dc ba 98
C_bin=(hex2bin("fe")+hex2bin("dc")+hex2bin("ba")+hex2bin("98"))
#          word D: 76 54 32 10
D_bin=(hex2bin("76")+hex2bin("54")+hex2bin("32")+hex2bin("10"))
print(A_bin)
print(B_bin)
print(C_bin)
print(D_bin)
arr=[]
for i in res:
	#print(i)
	arr.append(i)
print("Arr=")

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

rows, cols = (32, 16)
# method 2 1st approach
arr = [[0]*cols]*rows
for i in range(32):
	arr[0][i]=1
	print(i)
"""
