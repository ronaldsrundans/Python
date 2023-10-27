def XORfunction(a,b):
        if(a==b):
                return 0
        else:
                return 1
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
def HammingCode(word, error):
	print("Message:")
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
	cars=[]
	for i in send_word:
		cars.append(i)
	#Parbauda kadai jabut Parity vertibam sanemtaja zina
	ParityValues(cars,parity_pos)
	print("Compared word:")
	print(cars)
	ParityCheck(send_word, cars, parity_pos)
	
word_arr=[[1,1,0,1,1,1,1],[1,0,0,1,0,0,0],[1,1,0,0,0,0,1],[1,1,0,1,1,0,1],[1,1,0,1,0,0,1]]
er_arr=[[0,1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,1,0,0,0]]
for i in range(5):
	HammingCode(word_arr[i],er_arr[i])
