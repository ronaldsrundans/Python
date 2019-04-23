def my_function(arr):
	#print(arr)
	n=0
	for i in range(4):
		for j in range(5):
			if(i!=j):
				if(arr[i]==arr[j]):
					#print(arr)
					n+=1
			else:continue
	return n


	
	
  

from array import *
c=0
arr = [5,7,8,9,0]
#print(arr)
res = [None] *5
for i in range(4):
	
	res[0]=arr[i]
	#print(arr[i])
	for j in range(5):
		res[1]=arr[j]
		#print(res)
		#print(arr[j])
		for k in range(5):
			res[2]=arr[k]
			#print(arr[k])
			for l in range(5):
				res[3]=arr[l]
				#print(arr[l])
				for m in range(5):
					res[4]=arr[m]
					#print(res)
					#c+=1
					if(my_function(res)<1):
						print(res)
						c+=1
						#print(my_function(res))
print(c)


