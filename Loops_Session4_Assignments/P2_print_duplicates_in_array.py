'''
WPP to print duplicate elements in array
'''

a=[4,5,4,3,2,7,89,3,99,100]
dict_a = {}
for i in a:
    if i not in dict_a:
        dict_a[i]=1
    else:
        dict_a[i]=dict_a[i]+1
print(dict_a)

#method2
new_a=[]
l=len(a)
for i in range(l):
    for j in range(i+1, l):
        if a[i]==a[j] and a[i] not in new_a:
            new_a.append(a[i])
print(new_a)

#method3
for i in range(len(a)):
    print(a[i], a.count(a[i]), end =", ")



