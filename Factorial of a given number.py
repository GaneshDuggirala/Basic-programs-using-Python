# Python program to print a factorial of a number

# 	---> Method-1 <---

n=int(input())
fact=1
while(n!=0):
	fact=fact*n
	n=n-1
print("Factorial of a given number is :",fact)


#	---> Method-2 <---

# Using Recursion 

 
def factorialprogram(fact,n):
	if(n==0):
		return fact
	fact=fact*n

	return factorialprogram(fact=fact,n=n-1)

n=int(input())
fact=1

print("Factorial of a given number is :",factorialprogram(fact,n))

