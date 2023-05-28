#--coding:utf8;--
#qpy:console
arr=["1","2","3","4","5","25"]
op=["+","-","*","/"]
num=52
res=""
for i in arr:
	#print(i)
	if (res==num):
		print ("Yes")
		break
	res=i
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
							res=eval((i+i1+j)+i2+k)
							if(res==num):
								print(i+i1+j+i2+k+"=")
								print(res)
								break
							for i3 in op:
								for x in arr:
									if((x==i) or (x==j) or (x==k)):
										continue
									else:
										res=eval(i+i1+j+i2+k+i3+x)
										if(res==num):
											print(i+i1+j+i2+k+i3+x+"=")
											print(res)
											break
										for i4 in op:
											for y in arr:
												if((y==i) or (y==j) or (y==k) or (y==x)):
													continue
												else:
													res=eval(i+i1+j+i2+k+i3+x+i4+y)
													if(res==num):
														print(i+i1+j+i2+k+i3+x+i4+y+"=")
														print(res)
														break
													for i5 in op:								
														for z in arr:
															if((z==i) or (z==j) or (z==k) or (z==x) or (z==y)):
																continue
															else:
																res=eval(i+i1+j+i2+k+i3+x+i4+y+i5+z)
																if(res==num):
																	print(i+i1+j+i2+k+i3+x+i4+y+i5+z+"=")
																	print(res)
																	break
						#elif (res==num):

"""

			
					for i3 in op:
            			for x in arr:
                			if((x==i) or (x==j) or (x==k)):
                    			continue
                			res=eval(str(res)+i3+str(x))
							if (res==num):
								print(str(i)+i1+str(j)+i2+str(k)+i3+str(x))
        						print (res)
        						break
							for i4 in op:
								for y in arr:							
                   	 				if((y==i) or (y==j) or (y==k) or (y==x)):
                        				continue
                    				res=eval(str(res)+i4+str(y))
									if (res==num):
										print(str(i)+i1+str(j)+i2+str(k)+i3+str(x)+i4+str(y))
        								print (res)
        								break
									for i5 in op:								
										for z in arr:
                       						if((z==i) or (z==j) or (z==k) or (z==x) or (z==y)):
                            					continue
											res=eval(str(res)+i5+str(k))
											if (res==num):
												print(str(i)+i1+str(j)+i2+str(k)+i3+str(x)+i4+str(y)+i5+str(z))
        										print (res)
        										break
											
                        #print( i, j,k,x,y,z)
						#found it!
                 # print(str(i)+i1+str(j)+i2+str(k)+i3+str(x)+i4+str(y)+i5+str(z))
                           
                             #if (res==num):
                               #  print (res)
                               #  break
                             #
                               
                                    
                                       
                                           # print(i1+i2+i3+i4+i5)
                                             #res=(eval(str(i)+i1+str(j)))
                                            # if(res==num):
                                               #  print(str(i)+i1+str(j))
                                               #  break
                                            
                                            
                        
        
    
print ("This is console module")
"""
				
