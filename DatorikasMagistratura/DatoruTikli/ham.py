#--coding:utf8;--
#qpy:console
def XORfunction(a,b):
        if(a==b):
                return 0
        else:
                return 1


word=[1,1,0,1,1,1,1]
error=[0,1,0,0,0,0,0]
r_word=[]
word_len=len(word)
parity_pos=[]
send_word=[]
print( "word=")
print(word)
print("Erorr=")
print(error)
for i in range(int(word_len/2+1)):
   # print(2i-1)
    parity_pos.append(2**i-1)
#print(parity_pos)
for i in word:
    #send_word.append()
    for j in parity_pos:
       # print(j)
        if(j==len(send_word)) :
            send_word.append(j)
    send_word.append(i)
#print(send_word)
for i in parity_pos:
    sum_par=0
    k=i+1
    k_pos=0
    bin_k=[]
    for j in range(len(parity_pos)):
        bin_k.append(k%2)
        if(k%2==1):
            break
        k=int(k/2)
        k_pos+=1
    #print("x=")
    for x in range(i+1,len(send_word),1):
        #print(x)
        l=x+1
        l_pos=0
        bin_l=[]
        for y in range(len(parity_pos)):
            bin_l.append(int(l%2))
            if(l_pos==k_pos and l%2==1):
                break
            l=int(l/2)
            l_pos+=1

        if(k_pos==l_pos):
            #print("Match x="+str(x))
            #print("Value="+str(send_word[x]))
            #print(bin_k)
            if(send_word[x]==1):
                sum_par+=1
   # print("i="+str(i))
    if (sum_par%2==0):
        send_word[i]=0
    else:
        send_word[i]=1
    #send_word[i]=666
print("transmitted word=")
print(send_word)
print("received word=") 
##add error
for i in error:
    #send_word.append()
    for j in parity_pos:
       # print(j)
        if(j==len(r_word)) :
            r_word.append(0)
    r_word.append(i)
#print(r_word)
# with error
for i in range(len(r_word)):
	send_word[i]=XORfunction(r_word[i],send_word[i])
print(send_word)

#erro correction
cars=[]
for i in send_word:
	cars.append(i)
#for i in parity_pos:
#	cars.pop(i)
for i in parity_pos:
    sum_par=0
    k=i+1
    k_pos=0
    bin_k=[]
    for j in range(len(parity_pos)):
        bin_k.append(k%2)
        if(k%2==1):
            break
        k=int(k/2)
        k_pos+=1
    #print("x=")
    for x in range(i+1,len(cars),1):
        #print(x)
        l=x+1
        l_pos=0
        bin_l=[]
        for y in range(len(parity_pos)):
            bin_l.append(int(l%2))
            if(l_pos==k_pos and l%2==1):
                break
            l=int(l/2)
            l_pos+=1

        if(k_pos==l_pos):
            #print("Match x="+str(x))
            #print("Value="+str(send_word[x]))
            #print(bin_k)
            if(cars[x]==1):
                sum_par+=1
            #print(x)
            #for x in range(len(send_word)):
                #y=x+1

                #if(y%2==0 AND y_pos==k_po0s)

        #k_counter+=1
        #if
    #print("end x")
   # print("sum="+str(sum_par))
   # print("i="+str(i))
    if (sum_par%2==0):
        cars[i]=0
        #send_word[i]=0
    else:
        #send_word[i]=1
        cars[i]=1
    #send_word[i]=666
print("received word=")
print(cars)
bin_error=[]
for i in parity_pos:
	bin_error.append(XORfunction(send_word[i],cars[i]))
print(bin_error)
error_pos=0
for i in range(len(bin_error)-1,0,-1):
	error_pos=error_pos+2**bin_error[len(bin_error)-i]
print(error_pos)
