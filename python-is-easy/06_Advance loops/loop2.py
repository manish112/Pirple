max_row=100
max_column=200

def board(row, col):

	if row>max_row or col >max_column:
		print("Sorry! Can't create board")
		return False
	print("")
	for i in range(row):
		if(i%2==0):
			for j in range(col):
				if(j%4==0 or j==col-1):
					print("|",end="")
				else:
					print(" ",end="")
			
		else:
			for k in range(col):
				print("-", end="")
		print("")
	return ""




board(70,84)
board(200,50)