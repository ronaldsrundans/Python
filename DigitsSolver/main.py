#--coding:utf8;--
#qpy:console
arr=["5","7","8","9","15","20"]
op=["+","-","*","/"]
num=341
res=""
for i in arr:
	#print(i)
	res=i
	if (res==num):
		print (res)
		break
	
	for i1 in op:
		for j in arr:
			if(i==j):
				continue
			else:
				res=eval(i+i1+j)
				if(res==num):
					print(i+i1+j+"=")
					print(res)
					break
				for i2 in op:
					for k in arr:
						if((i==k)or(j==k)):
							continue
						else:
							res=eval("("+i+i1+j+")"+i2+k)
							if(res==num):
								print(i+i1+j+i2+k+"=")
								print(res)
								break
							for i3 in op:
								for x in arr:
									if((x==i) or (x==j) or (x==k)):
										continue
									else:
										res=eval("(("+i+i1+j+")"+i2+k+")"+i3+x)
										if(res==num):
											print(i+i1+j+i2+k+i3+x+"=")
											print(res)
											break
										for i4 in op:
											for y in arr:
												if((y==i) or (y==j) or (y==k) or (y==x)):
													continue
												else:
													res=eval("((("+i+i1+j+")"+i2+k+")"+i3+x+")"+i4+y)
													if(res==num):
														print(i+i1+j+i2+k+i3+x+i4+y+"=")
														print(res)
														break
													for i5 in op:								
														for z in arr:
															if((z==i) or (z==j) or (z==k) or (z==x) or (z==y)):
																continue
															else:
																res=eval("(((("+i+i1+j+")"+i2+k+")"+i3+x+")"+i4+y+")"+i5+z)
																#print("res+")
																#print(res)
																if(res==num):
																	print(i+i1+j+i2+k+i3+x+i4+y+i5+z+"=")
																	print(res)
																	break
			

