def XORfunction(a,b):
        if(a==b):
                return 0
        else:
                return 1
def CRCfunction(frame,generator):
	print("CRC Message:")
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
			#Dala tikai tad, ja pirmajā pozīcijā ir "1"
			if(arr[0]==1):
				for i in range(len_remainder):
					arr[i]=(XORfunction(arr[i],generator[i]))
			#Ja pirmajā pozīcijā ir "0", tad dala ar virkni "000.."
			else:
				for i in range(len_remainder):
					arr[i]=(XORfunction(arr[i],0))
			
			arr.pop(0)		
	#Nomaina pēdējos bitus ar rezultātu
	for i in range(0,len(arr), 1):
		frame[len_frame-len(arr)+i]=arr[i]
	print("Transmitted message:")
	print(frame)
def AddErorr(send_word,error,parity_pos):
	r_word=[]
	#Hamminga kodā pievieno paritātes bitus error masīvā, bet CRC neko nedara šis cikls
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
	len_remainder=len(generator)
	len_frame=len(frame)
	remainder=[]
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
		for j in checksum:
			#Skaita "0" checksumā
			if(j==0):
				checkcounter+=1
		if (len(checksum)==checkcounter):
			#Ja checksumā visi ir "0", tad ir izlabota saņemtā ziņa
			print("Fixed error")
			print(tmp)
			break
		else:
			tmp[i+1]=var
			#print("Done")

def CRC(word,key,error):
	CRCfunction(word,key)
	arr=[]
	fix=0
	print("Error:")
	print(error)
	AddErorr(word,error,[])
	print("Received message:")
	print(word)
	CRCdecode(word,key,arr)
	print("Parity check:")
	print(arr)
	for i in arr:
		if(i==1):
			fix=1
	if (fix==1):
		fixError(word,key,arr)
	fix=0
	print("\n")
###CRC# EXAMPLES
words=[[1,0,0,1,0,0],[1,1,0,1,0,1,1,0,1,1],[1,1,0,1,0,1,1,0,1,1],[1,0,1,1,0,0,1,1],[1,0,0,1,0,0]]
keys=[[1,1,0,1],[1,0,0,1,1],[1,0,0,1,1],[1,0,0,1,1],[1,0,0,1,1]]
errors=[[0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0]]
for i in range(5):
	CRC(words[i], keys[i], errors[i])
	("Done")
