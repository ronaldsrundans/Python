from array import*
T=[[1,2,3,4],[5,6,7,8],[9,10,11]]
#1001000
#1100001
#1101101
#1101101
#1101001
#1101001
word=[1,1,0,0,0,0,1]
word_len=len(word)
parity_pos=[]
send_word=[]
parity_len=int(word_len/2+1)
print(word)
for i in range(parity_len):
#	print(2**i-1)
	parity_pos.append(2**i-1)
print(parity_pos)


for i in word:
	for j in parity_pos:
		if (j==len(send_word)):
			send_word.append(666)
	send_word.append(i)
print("pirms parity_check=")
print(send_word)
#print("len=")
#print(len(send_word))	
len_send_word=len(send_word)
for i in parity_pos:		#parity check (vertibas i no 0-3 un k no 1-4)
	#print("k=")		#parity pos pārveido par bin skaitli
	#print(i+1)
	k=i+1
	bin_k=[]
	k_pos=0
	parity_sum=0
	#print("bin_k=")
	for j in range(parity_len):	# vertibas j no 0-3
		#print(int(k%2))
		bin_k.append(int(k%2))
		if(k%2==1):
			break
		k_pos+=1
		k=k/2
	#print("k_pos=")
	#print(k_pos)
	for x in range(i+1,len_send_word,1):	#parbauda vertibas no i+1 līdz send_word beigām (lai nepārbauda sevi)(pozicijas skaita no 1)
		l_pos=0
		l=x+1
		bin_l=[]
		#print(x%2)
		for y in range(parity_len):	#skaita no 0-3
			bin_l.append(int(l%2))
			if(l%2==1):
				break
			l=l/2
			l_pos+=1
		#print("l_pos=")
		#print(l_pos)
		if(l_pos==k_pos):
			#print("match!")
			#print("parity pos(no0)=")
			#print(i)
		#	print(x)
			
			#print(bin_k)
			#print(bin_l)
			if(send_word[x-1]==1):
				parity_sum+=1 
	#print(bin_k)
	if (parity_sum%2==0):
		send_word[i]=0	#šeit ieliek paritates vērtību t.i. pāris=0 nepāris=1
	else: send_word[i]=1
	print("next")
print(send_word)
#	for i in parity_pos:
#		if(j==i):
#			transmitted_word.append(i)
#			large+=1
#			
#		transmitted_word.append(word[j])
#	print(word[j])
#for k in transmitted_word:
#	print(k)

#y=len(T)
#print(y)
#z=len(T[])
#lenght=11
#rows=lenght/4
#cols=lenght-rows*4
#for j in range(4):
#	for k in range(4):
#		print(T[j][k])
transmitted_word=[]
erorr=[]
received_word=[]
error_check=[]
corrected_word=[]
#for i in range(0,16,1):
#	print(i)
#def parity_check():
#print("Hello World!")
