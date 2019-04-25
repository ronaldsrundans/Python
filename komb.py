def my_function(arr):
	#print(arr)
	n=0
	for i in range(4):
		for j in range(i+1,5):
			if(arr[i]==arr[j]):
				n+=1
			else:continue
		if(n>0):
			break

	return n
#a)Cik iesakas ar "98"?
#b)Cik dalas ar 5?
#c)Cik beidzas ar "78"?
#d)Cik dazadi gadijumi?	
from array import *
a=0
b=0
c=0
d=0
arr = [5,7,8,9,0]
#print(arr)
res = [None] *5
for i in range(4):
	res[0]=arr[i]
	for j in range(5):
		res[1]=arr[j]
		for k in range(5):
			res[2]=arr[k]
			for l in range(5):
				res[3]=arr[l]
				for m in range(5):
					res[4]=arr[m]
						if(my_function(res)<1):
							d+=1
						if(res[0]==9 and res[1]==8):
							a+=1
							print("a=")
							print(res)
						if(res[4]==5 or res[4]==0):
							b+=1
							print("b=")
							print(res)
						if(res[3]==7 and res[4]==8):
							c+=1
							print("c=")
							print(res)
print(a)
print(b)
print(c)
print(d)

