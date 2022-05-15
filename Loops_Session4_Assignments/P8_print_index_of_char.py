'''
WPP to print the index of the character in a string
'''

s="This is my string"
for i, a in enumerate(s):
    print(a, i, end =", ")
print()
#method2

print(s.find('m'))
print(s.index('s'))

