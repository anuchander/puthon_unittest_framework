example_set={'jan', 'feb', 'mar'}
print(example_set)

example_set.add('apr')
print(example_set)

example_set.update(['may', 'june', 'july', 'aug', 'jan'])
print(example_set)

example1=set(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
print(example1)

example1.remove('Tue')
print(example1)

example1.discard('Wed')
print(example1)

#difference between discard and remove, if element is not there discard does not throw an error, but remove throws error
example1.discard('Tue')
print(example1)

weekdays={'Mon', 'Tue','Wed', 'Thu', 'Fri'}
weekends={'Fri', 'Sat', 'Sun'}

print(weekdays.union(weekends))
print(weekdays.intersection(weekends))
print(weekdays.difference(weekends))

#frozen set - cannot add, or update, remove from set
example1_days=frozenset(['jan', 'feb', 'mar'])
print(example1_days)

#default arguments
def stu_entry(section='7A'):
    name=input("Enter your name")
    age=input("Enter your age")
    id=input("Enter your id")
    #section=input("Enterr yourr section")
    print("Student ", name, "is of agev", age, "with idv", id, "in section ", section)
    print()

def name(a1, a2):
    print(a1," ", a2)
    return a1+a2

#keywords as arguments
result=name(a2='Shah', a1='Payal')
print(result)
print(type(name("4","5")))

def printnames(*name):
    for i in name:
        print(i, end=" ")

printnames("Sandhya", "Mithun", "Jnanesh", 5)
print()

for i in range(3):
    stu_entry()

