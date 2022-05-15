'''
WPP to swap cases of a given string eg. pyTHoN output: PYthOn
'''

s='pyTHoN'
print("The given string is: ", s)
for a in s:
    if a.isupper():
        print(a.lower(), end =" ")
    elif a.islower():
        print(a.upper(), end=" ")
