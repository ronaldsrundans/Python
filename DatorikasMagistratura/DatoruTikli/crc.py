def XORfunction(a,b):
        if(a==b):
                return 0
        else:
                return 1
def comparefunction(a,b):
	for i in range(0,4,1):
		print(i)

def CRCfunction(frame,generator):
	len_remainder=len(generator)
	for i in range(1,len_remainder,1):
		frame.append(0)
	len_frame=len(frame)
	print("Frame=")
	print(frame)
	arr=[]
	remainder=[]
	for j in range(len_frame):
		arr.append(frame[j])
		if(len(arr)==len_remainder):
			if(arr[0]==1):
				for i in range(len_remainder):
					#print(arr[i])
					arr[i]=(XORfunction(arr[i],generator[i]))
			else:
				for i in range(len_remainder):
					arr[i]=(XORfunction(arr[i],0))
			
			arr.pop(0)		
		#print(arr)
		#Nomaina pēdējos ar rezultātu
	for i in range(0,len(arr), 1):
		frame[len_frame-len(arr)+i]=arr[i]
	print("Frame=")
	print(frame)
def CRCdecode(frame, generator):
	len_remainder=len(generator)
	#for i in range(1,len_remainder,1):
	#	frame.append(0)
	len_frame=len(frame)
	print("Frame=")
	print(frame)
	arr=[]
	remainder=[]
	#for i in range(len_remainder):
	#	arr.append(frame[i])
	#print(arr)
	for j in range(len_frame):
		#print("j=")
		#print(j)
		arr.append(frame[j])
		#print(arr)
		if(len(arr)==len_remainder):
			if(arr[0]==1):
				for i in range(len_remainder):
					#print(arr[i])
					arr[i]=(XORfunction(arr[i],generator[i]))
			else:
				for i in range(len_remainder):
					arr[i]=(XORfunction(arr[i],0))
			
			arr.pop(0)		
		#print(arr)
		#Nomaina pēdējos ar rezultātu
	#for i in range(0,len(arr), 1):
	#	frame[len_frame-len(arr)+i]=arr[i]
	print("Arr=")
	print(arr)
def fixError(frame,generator):
	print("Hello!")
	
word=[1,0,0,1,0,0]
error=[0,1,0,0,0,0,0]
key=[1,1,0,1]

word2=[1,0,0,0,0,0,0,0,1]
key2=[]
word3=[1,1,0,1,0,1,1,0,1,1]
key3=[1,0,0,1,1]
word4=[1,0,1,1,0,0,1,1]
key4=[1,0,0,1,1]
r_word=[]
word_len=len(word)
parity_pos=[]
send_word=[]
fixError(word2,key)
#print( "word=")
#print(word)
#print("Key=")
#print(key)
CRCfunction(word,key)
CRCdecode(word,key)
CRCdecode(word2,key)
#print("word3=")
#CRCfunction(word3,key3)
#CRCdecode(word3,key3)
#CRCfunction(word4, key4)
#CRCdecode(word4,key4)
