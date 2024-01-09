# Method 1
# --------------

num= int(input("Enter the size of the array: "))

arr=[]
print("Enter the elements of the array: ")
for i in range(num):
  arr.append(int(input()))
  
print("The elements are: ")

for i in arr:
  print(i,end=" ")
  
  
