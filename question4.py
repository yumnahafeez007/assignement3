#Write a Python program to sum all the numeric items in a dictionary


dictionary = {'a':'2', 'b':'5','c' : 'hello world'}
result = 0

for x in dictionary:
	if (dictionary[x].isnumeric()) == True :
		convert_in_integer = int(dictionary[x])
		result = result + convert_in_integer


print(result) 
