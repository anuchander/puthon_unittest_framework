'''
WPP to sort the array in ascending order without input methods
'''

a=[32,21,6,8,17, 7,100,99]
print("The given array is: ", a)
for i in range (len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp

print("The sorted array is: ", a)