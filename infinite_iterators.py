'''
infinite iterators
1. count()
2. repeat()
3. cycle()
'''

'''
Terminating iterators
1. accumulate()
2. chain()
3. isslice()
4. zip_longest()

'''
import itertools
from itertools import count

#count() of infinite iterator
for i in count(10, 5):
    if(i>50):
        break
    else:
        print(i, end=" ")
print()

#repeat() of infinite iterator
list1 = [1,2,3,4,5]
rep = itertools.repeat(list1)
print(next(rep))
print(next(rep))

#repeat()
rep = itertools.repeat(10, 5)
for i in range(0, 5):
    print(next(rep), end =" ")
print()

#cycle()
list1=[1,2,3,4,5]
rep = itertools.cycle(list1)
for i in range(0,10):
    print(next(rep), end = " ")
print()

#accumulate()
print(list1)
print(list(itertools.accumulate(list1)))
rep=itertools.accumulate(list1)
print(list(rep))
print()

#chain()
list1=[1,2,3,4,5]
list2=[6,7]
list3=[8]
rep = itertools.chain(list1, list2, list3)
print(list(rep))

#isslice()
list1=[1,2,3,4,5]
print(list(itertools.islice(list1, 3))) #prints 3 elements
print(list(itertools.islice(list1, 2,4))) # starts at 2nd element and prints till 4th element
print(list(itertools.islice(list1, 0,5,2))) # starts at 0 element, prints till 5th element and steps 2


