#--coding:utf8;--
#qpy:console
word=[1,1,0,1,1,1,1]
word_len=len(word)
parity_pos=[]
send_word=[]
print( "word=")
print(word)
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
        send_word[i]=0
    else:
        send_word[i]=1
    #send_word[i]=666
print("received word=")
print(send_word)
