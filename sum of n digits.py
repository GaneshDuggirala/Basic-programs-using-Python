# Initialize the num

num=int(input())
# convert it into string

s=str(num)
temp=0    #Initialize Temporary variable

# Use for loop to iterate the string
for i in s:
    i=int(i)  # convert string to Integer
    temp=temp+i     # Add to Temp

# print the result

print(temp)