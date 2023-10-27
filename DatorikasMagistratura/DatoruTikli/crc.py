def XORfunction(a,b):
        if(a==b):
                return 0
        else:
                return 1
#def comparefunction(a,b):
#	for i in range(0,4,1):
#		print(i)

def CRCfunction(frame,generator):
	print("Message:")
	print(frame)
	len_remainder=len(generator)
	#Pagarina bitu virknes gala pievieno "0" vertibas
	for i in range(1,len_remainder,1):
		frame.append(0)
	len_frame=len(frame)
	print("Padded message:")
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
	print("Transmitted message:")
	print(frame)
def AddErorr(send_word,error,parity_pos):
	r_word=[]
	for i in error:
		for j in parity_pos:
			if(j==len(r_word)) :
				r_word.append(0)
		r_word.append(i)
	for i in range(len(r_word)):
		#Kļūdu rada XOR funkcija, kas pārveido 0->1 vai 1->0, ja Error masīvā ir "1" 
		send_word[i]=XORfunction(r_word[i],send_word[i])
	print(send_word)
def CRCdecode(frame, generator,arr):
	#print("Decode")
	len_remainder=len(generator)
	#for i in range(1,len_remainder,1):
	#	frame.append(0)
	len_frame=len(frame)
	#print("Received message:")
	#print(frame)
	#arr=[]
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
	#print("Parity check:")
	#print(arr)
def fixError(frame,generator,arr):
	#print("Fix error!")
	tmp=[]
	#Nokope sanemto zinu
	for i in frame:
		tmp.append(i)
	#print(tmp)
	checksum=[]
	checkcounter=0
	len_frame=len(frame)
	#Cikla sanemtai zinai mainis katru vertibu un parbaudis checksum
	for i in range(len_frame-1):
		var=tmp[i+1]
		checkcounter=0
		#Nomaina uz pretejo vertibu
		tmp[i+1]=(XORfunction(tmp[i+1],1))
		CRCdecode(tmp,generator,checksum)
		#print("Checksum:")
		#print(checksum)
		for j in checksum:
			#Skaita "0" checksuma
			if(j==0):
				#print(j)
				checkcounter+=1
		#print(checkcounter)
		if (len(checksum)==checkcounter):
			#Ja checksum visi ir "0", tad ir izlabota zina
			print("Fixed error")
			#print(len(checksum))
			print(tmp)
			break
		else:
			tmp[i+1]=var
			print("Done")

def CRC(word,key,error):
	CRCfunction(word,key)
	arr=[]
	print("Error:")
	print(error)
	AddErorr(word,error,[])
	print("Received message:")
	print(word)
	CRCdecode(word,key,arr)
	print("Parity check:")
	print(arr)
	fixError(word,key,arr)



words=[[1,0,0,1,0,0],[1,0,0,0,0,0,0,0,1],[1,1,0,1,0,1,1,0,1,1],[1,0,1,1,0,0,1,1]]
keys=[[1,1,0,1],[1,0,0,1,1],[1,0,0,1,1],[1,0,0,1,1],[1,0,0,1,1]]
errors=[[0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0]]
for i in range(5):
	print(i)
	CRC(words[i], keys[i], errors[i])
