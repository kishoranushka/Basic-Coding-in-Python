# Write a program to print all numbers between two intervals, namely low and high. But, with a special condition that if any number in the range while getting printed becomes divisible by 13 then you must not print anything further and stop. (Do this using the Break Statement)

low=int(input("Enter first number: "))
high= int(input("Enter second number: "))

for i in range(low,high+1):
  print(i)
  if (i%13==0):
    break