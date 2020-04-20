def compare_data(a,b,c):
	a1=int(a)
	b1=int(b)
	c1=int(c)
	
	if a1==b1:
		return True
	elif a1==c1:
		return True
	elif b1==c1:
		return True
		
	return False



print(compare_data(6,5,4))

print(compare_data(6,5,5))

print(compare_data(6,5,"5"))

print(compare_data(6,6,6))