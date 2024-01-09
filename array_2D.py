# Method 1
# -------------

# row=int(input("enter the no. of row: "))
# col=int(input("enter the no. of column: "))

# matrix=[]
# print("Enter the elements of the array in row wise: ")

# for i in range(row):
#   a=[]
#   for j in range(col):
#     a.append(int(input()))
    
#   matrix.append(a)
  
  
# print("The matrix is : ")
# for i in range(row):
#   for j in range(col):
#     print(matrix[i][j],end=" ")
#   print()



# Method 2
# ------------

row=int(input("enter the no. of row: "))
col=int(input("enter the no. of column: "))

matrix=[]

print("Enter the elements of the matrix row wise : ")
matrix=[[int(input()) for x in range(col)]for y in range(row)]

for i in range(row):
  for j in range(col):
    print(matrix[i][j],end=" ")
  print()


