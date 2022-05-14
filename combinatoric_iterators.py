'''
combinatoric iterators
1.product()
2.permutations()
3.combinations()
4.combinationwithreplacement()

'''

import itertools
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

list1 = [4,5,6]
list2=[1,2,3,4,5,6,7,8,9,10]
print(list(product(list2, 'C')))

#permutations
print(list(permutations(list1, 3))) # 3 represents the number of elements in the permutations

#combinations
print(list(combinations(list1, 2))) # permutations contain repetitions, but combinations does not contain repetitions

#combinations with replacement
print(list(combinations_with_replacement(list1, 2)))


