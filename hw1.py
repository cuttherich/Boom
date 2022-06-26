#! /bin/python3

var = 26
var1 = 213
var2 = 485

if var > var1 and var > var2:
	print("the biggest is", var)
	if var1 < var2:
		print("the smallest is", var1)
	else:
		print("the smallest is", var2)
elif var1 > var and var1 > var2:
	print("the biggest is ", var1)
	if var < var2:
		print("the smallest is", var)
	else:
		print("the smallest is", var2)
#elif var2 > var and var2> var1:
	#print(var2)
else:
	print("the biggest is", var2)
	if var < var1:
		print("the smallest is", var)
	else:
		print("the smallest is", var1)
