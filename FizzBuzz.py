number = 1
while (number < 101):
	if (number % 3 == 0 and number % 5 == 0):
		print ("FizzBuzz")
	else:
		if (number % 3 == 0):
			print ("Fizz")
		  
		if (number % 5 == 0):
			print ("Buzz")
        
		if (number % 3 != 0 and number % 5 != 0):
			print (number)
	number += 1