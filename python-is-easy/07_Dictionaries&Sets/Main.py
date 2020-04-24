"""
This is a python code which has attributes 
about a song
"""

def checkInput(key,value):
	if key in album:
		if value!=str(album[key]):
			return False
		else:
			return True
	else:
		return False

album={'Artist':"Dave Brubeck", 'Genre':"Jazz", 'DurationInSeconds': 328, 'year':2015, 'ratings':4.5,'songname':"Hello"}



for key in album:
	print(key+" "+str(album[key]))




key=input('Enter Key: ')


value=input("Enter value: ")

print(checkInput(key, value))






