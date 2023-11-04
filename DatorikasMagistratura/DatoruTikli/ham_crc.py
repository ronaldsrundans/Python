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
	#print(send_word)
def CRCdecode(frame, generator,arr):
	len_remainder=len(generator)
	len_frame=len(frame)
	remainder=[]
	for j in range(len_frame):
		arr.append(frame[j])
		if(len(arr)==len_remainder):
			if(arr[0]==1):
				for i in range(len_remainder):
					arr[i]=(XORfunction(arr[i],generator[i]))
			else:
				for i in range(len_remainder):
					arr[i]=(XORfunction(arr[i],0))
			
			arr.pop(0)
def fixError(frame,generator,arr):
	tmp=[]
	#Nokopē sanemto ziņu
	for i in frame:
		tmp.append(i)
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

def PaddingParity(word,send_word,parity_pos):
	#return 0
	word_len=len(word)
	#Aizpilda masivu ar paritātes bitu adresēm, kur tos likt sūtāmajā ziņā (0,1,3,...) 
	for i in range(int(word_len/2+1)):
    		parity_pos.append(2**i-1)
	#Rezervē vietu paritātes bitiem sūtāmajā ziņā
	for i in word:
    		for j in parity_pos:
        		if(j==len(send_word)) :
            			send_word.append(j)
    		send_word.append(i)
def ParityCheck(send_word, cars, parity_pos):
	bin_error=[]
	for i in parity_pos:
		bin_error.append(XORfunction(send_word[i],cars[i]))
	print("Parity check:")
	print(bin_error)
	error_pos=0
	for i in range(0,len(bin_error),1):
		error_pos=error_pos+(2**i*bin_error[i])
	if (error_pos==0):
		print("No errors found")
	else:
		print("Found error in position:")
		print(error_pos)
		print("Corrected word:")
		send_word[error_pos-1]=XORfunction(send_word[error_pos-1],1)
		print(send_word)
def ParityValues(send_word,parity_pos):
	#Aprēķina katra paritātes bita vērtību šajā ciklā
	for i in parity_pos:
		sum_par=0
		k=i+1
		k_pos=0
		bin_k=[]
		#Paritātes bita adresi pārveido binārā skaitlī (0001, 0010, ...)
		for j in range(len(parity_pos)):
			bin_k.append(k%2)
			if(k%2==1):
				break
			k=int(k/2)
			k_pos+=1
		#Meklē pozīcijas sūtāmajā tekstā, kuru adresēs binārā pierakstā atrodas vērtība "1"
		#Piemēram, ja paritātes bits ir 0010, tad skatās uz 1010, 1111,0111,...
		for x in range(i+1,len(send_word),1):
			l=x+1
			l_pos=0
			bin_l=[]
			for y in range(len(parity_pos)):
            			bin_l.append(int(l%2))
				#Ja atrod adresi ar "1" īstaja vietā (binārā formā), meklē 0 001 un atrod 0101
            			if(l_pos==k_pos and l%2==1):
                			break
            			l=int(l/2)
            			l_pos+=1
			#Skaita "1" simbolus attiecīgajās pozīcijās
			if(k_pos==l_pos):
				if(send_word[x]==1):
                			sum_par+=1
		#Ja simbolu "1" skaits ir pāra skaitlis, tad raksta "0"
		if (sum_par%2==0):
			send_word[i]=0
		#Ja simbolu "0" skaits ir nepāra skaitlis, tad raksta "1"
		else:
        		send_word[i]=1

def HammingCode(word, error):
	print("HammingCode Message:")
	print(word)
	parity_pos=[]
	send_word=[]
	PaddingParity(word,send_word, parity_pos)
	ParityValues(send_word, parity_pos)	
	print("Transmitted word:")
	print(send_word)
	print("Error:")
	print(error)
	print("Received word:")
	AddErorr(send_word,error, parity_pos)
	#Sūtāmajā vārdā pievieno kļūdu(nemaina paritātes bitu vērtības	
	print(send_word)
	compare=[]
	for i in send_word:
		compare.append(i)
	#Parbauda kadai jabut Parity vertibam sanemtaja zina
	ParityValues(compare,parity_pos)
	print("Compared word:")
	print(compare)
	ParityCheck(send_word, compare, parity_pos)
	print("\n")
#Hamming Code #EXAMPLES	
word_arr=[[1,1,0,1,1,1,1],[1,0,0,1,0,0,0],[1,1,0,0,0,0,1],[1,1,1,1,1,1,1],[0,0,0,0,0,0,0]]###Tiek labotas tikai kļūdas sūtamajā ziņā. Paritātes bitu vērtību izmaiņas netiek apskatītas.
er_arr=[[0,1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,1,1,1,0],[0,0,0,1,0,0,0]]###"1" norāda, kur būs kļūda sūtāmajā ziņā (pirms padding). Nelabo pareizi, ja ir vairāki "1"
for i in range(5):#Nokarās programma, ja dauzi "1" err_arr 
	HammingCode(word_arr[i],er_arr[i])
###CRC# EXAMPLES
words=[[1,0,0,1,0,0],[1,1,0,1,0,1,1,0,1,1],[1,1,0,1,0,1,1,0,1,1],[1,0,1,1,0,0,1,1],[1,0,0,1,0,0]]
keys=[[1,1,0,1],[1,0,0,1,1],[1,0,0,1,1],[1,0,0,1,1],[1,0,0,1,1]]
errors=[[0,1,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]]###"1" norāda, kur būs kļūda sūtāmajā ziņā(pēc padding). Nelabo pareizi, ja ir vairāki "1"
for i in range(5):#dažreiz neizlabo ziņu, arī gadījumos, ja ir tikai 1 bits nomainīts saņemtajā ziņā
	CRC(words[i], keys[i], errors[i])
	("Done")
