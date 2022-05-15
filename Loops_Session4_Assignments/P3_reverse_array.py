'''
WPP to print reverse of the given array
'''

a=[4,6,7,2,3,99,121,100]
print("The given array is:", a)

#method1
for i in range(len(a)-1, -1, -1):
    print(a[i], end =" ")
print()

#method2
print(a[::-1])
