#                    ------>  Method-1  <------

# Swapping of Two Number using Temp variable


# INPUTS

num1=int(input())
num2=int(input())

# Initialize temp variable

temp = 0

temp = num1  # num1 is storing in temp
num1 = num2  # num2 is storing in num1
num2 = temp  # temp is storing in num2

print("Swapped num1 is : ",num1)
print("Swapped num2 is : ",num2)


#                   ------>  Method-2  <------


# Swapping of Two Number using two variables

num1,num2=map(int,input().split())    #Inputs using map function

#Inputs : 23 55

num1,num2=num2,num1

#At a time  swapping two variables

print("Swapped variable 1 : ",num1)
print("Swapped variable 2 : ",num2)
