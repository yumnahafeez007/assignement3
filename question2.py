# Write a program to check if there is any numeric value in list using for loop

arr = ['abc','ymk','2','458','hhh']

for x in arr:
	if (x.isnumeric()) == True:
		print(x + ' is numeric value')