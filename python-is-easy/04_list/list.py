myUniqueList=[]
myLeftovers=[]

def addThings(value):
	if value in myUniqueList:
		addLeftOvers(value)
		return False
	else:
		myUniqueList.append(value)
		return True
		

def addLeftOvers(val):
	myLeftovers.append(val)
	
	
	
print(addThings("test"))
print(addThings("sky"))
print(addThings("blue"))
print(addThings("BLUE"))
print(addThings("test"))
print(addThings(1))
print(addThings(1.0))
print(myUniqueList)
print(myLeftovers)

