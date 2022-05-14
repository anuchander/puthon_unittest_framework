import itertools

list1 = [1,2,3,4,5]
list2 = ['t', 'e', 'k', 'a', 'r', 'c', 'h']
listadd = zip(list1,list2)
for i in range (0, len(list1)):
    print(next(listadd))

#zip_longest()
list2=[4,5,6]
list3=[8,9,10,4]
print(list(itertools.zip_longest(list2,list3, fillvalue=0)))