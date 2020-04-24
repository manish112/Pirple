def prime(number):
	isPrime=1
	
	for i in range(2,number):
		if number%i==0:
			isPrime=0
		
	if isPrime==1:
		return "Prime "
	
	return ""
	
	
for i in range(1,101):
		flag=0
		
		print(prime(i),end="")
		if i%3==0:
			print("Fizz", end="")
			flag=1
		
		if i%5==0:
			print("Buzz", end="")
			flag=1
			
		
		
		
		if flag==0:
			print(i)
			continue
		
		flag=0
			
			
		print("")
			
	
