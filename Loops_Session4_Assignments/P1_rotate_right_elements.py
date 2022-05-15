'''
WPP to rotate to right elements in the array. Read the rotation.
input=[1,2,3,4] output=[4,1,2,3]

'''
a=[1,2,3,4]
print("The given array is:", a)
l=len(a)
last_element=a[l-1]
print("The last element is:", last_element)
for i in range(len(a)-2, -1, -1):
    a[i+1]=a[i]
a[0]=last_element

print(a)
