'''
WPP to print pronic numbers from 1 to 100
eg: 1(1+2), 2(2+3)
'''

for i in range(1,100):
    print(i, end="")
    print("(", end ="")
    print(i, end = "")
    print("+", end="")
    print(i+1, end="")
    print(")", end =", ")

