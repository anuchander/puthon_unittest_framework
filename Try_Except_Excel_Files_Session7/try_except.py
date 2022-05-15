try:
    a=int(input("Enter value for a: "))
    b=int(input("Enter value for b: "))
    c=a/b
    print("%d%d=%d" %(a,b,c))
    try:
        c=a*b
    except:
        print("nested try except block")
except (ZeroDivisionError, ArithmeticError):
    print("Cant divide by zero")
else:
    print("Try block completed!")
finally:
    print("Printing finally block code")

