'''
WPP to add two 3x3 matrix a b to c=a+b
'''
#assign the matrix:
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[[0,0,0],[0,0,0],[0,0,0]]
#print the matrix:
for i in range(3):
    for j in range(3):
        print(a[i][j], end=" ")
    print()
print()
for i in range(3):
    for j in range(3):
        print(b[i][j], end=" ")
    print()
print()
for i in range(3):
    for j in range(3):
        c[i][j]=a[i][j]+b[i][j]
        print(c[i][j], end=" ")
    print()