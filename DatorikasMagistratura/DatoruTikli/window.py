#print('Enter your name:')
x=''
window=4
arr1=[0,1,2,3,4,5,6,7,8,9]
arr2=[]
while (x!='q'):
	#for i in arr1:
	print(arr1)
	print(arr2)
	if (x==''):
		print("Press ENTER to continue!")
	elif (x=='s'):
		print("Send it!")
		print("->")
		
	elif (x=='k'):
		print("Kill it!")
	elif (x=='r'):
		print("Reset")
		arr2=[]
#	elif (x==''):
#		print("Nothing")
	else :
		print("Unknown!")
	#print(arr1)
	#print(arr2)
	print("Press 'r' to reset")
	print("Press 's' to send new")
	print("Press 'k' to kill packet")
	print("Press 'q' to quit")
	x = input()
	#print('Hello, ' + x) 
