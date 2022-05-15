'''
Add 'ing' at the end of a given string(length should be atleast 3). If the given string already ends with 'ing'
then add 'ly' instead.If the string length of the given string is less than 3, leave it unchanged
'''

s='adding'
s1='ab'
s2='test'

if len(s2)<3:
    print(s2)
elif s2[-3:]=='ing':
    print(s2+'ly')
else:
    print(s2+'ing')
