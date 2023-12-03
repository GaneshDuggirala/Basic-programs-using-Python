# python program to print simple intrest and compound intrest

# Simple Intrest

p=int(input())  # Principle
t=int(input())  # Time Period
r=float(input())  # Rate of Intrest

si=(p * t * r)/100 # simple intrest formula

print("The Simple Intrest is :",si)


# Compound Intrest

amount=p * (pow((1 + r / 100), t)) # compound intrest formula
ci=amount-p

print("The compound Intrest is :",ci)
