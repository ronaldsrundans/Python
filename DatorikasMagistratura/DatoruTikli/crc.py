#--coding:utf8;--
#qpy:console
def XORfunction(a,b):
        if(a==b):
                return 0
        else:
                return 1
def comparefunction(a,b):
	for i in range(0,4,1):
		print(i)
#def modulo2division():

def CRCfunction(frame,generator):
	#print(frame)
	#print(generator)
	len_remainder=len(generator)
	for i in range(1,len_remainder,1):
		frame.append(0)
	len_frame=len(frame)
	print("Frame=")
	#for i in frame:
	#	print(i)
	print(frame)
	arr=[]
	remainder=[]
	#for i in range(len_remainder):
	#	arr.append(frame[i])
	#print(arr)
	for j in range(len_frame):
		print("j=")
		print(j)
		arr.append(frame[j])
		if(len(arr)==len_remainder):
			for i in range(len_remainder):
				print(arr[i])
				arr[i]=(XORfunction(arr[i],generator[i]))
			arr.pop(0)		
		print(arr)
#arr.append(frame[j+len_remainder])
"""		print("Arr=")
		print(arr)
		for i in range(len_remainder):
			#if (arr[0]==0):
			#	break
			#else:
			print(str(arr[i])+"   XOR "+str(generator[i]))
			arr[i]=(XORfunction(arr[i],generator[i]))
			print(arr[i])
			#print(XORfunction(arr[i],generator[i]))
		arr.append(frame[j+len_remainder])			
		arr.pop(0)
"""		#print(arr)
		
#	print(arr)
			#remainder.append()
#	for i in range(len_frame-len_remainder): 	
#		print("Gen=")
#		for j in range(len_remainder):
#			print(XORfunction(frame[i+j],generator[j]))
			#print(j)
	
#	return 0
word=[1,0,0,1,0,0]
error=[0,1,0,0,0,0,0]
key=[1,1,0,1]

r_word=[]
word_len=len(word)
parity_pos=[]
send_word=[]
#print( "word=")
#print(word)
#print("Key=")
#print(key)
CRCfunction(word,key)
