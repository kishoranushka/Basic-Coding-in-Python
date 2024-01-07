import math

num=int(input("enter a number: "))

sqrRoot= math.sqrt(num)
cubeRoot= math.cbrt(num)
sqr= math.pow(num,2)
cube= math.pow(num,3)

root=num**(1/5)

print("Square root is : ",sqrRoot)
print("Cube root is : ",cubeRoot)
print("square is : ",sqr )
print("Cube is : ",cube )
print("1/5th root is : ",root )