
def demo1():
    for i in range(5):
        if (i%2==0):
            yield i

for i in demo1():
    print(i)

#example 2 generate squares of numbers
def squares():
    for i in range(10):
        yield i*i

values = squares()
for i in values:
    print(i, end=" ")

#2nd way of calling the sqaures genrator
print()
for i in squares():
    print(i, end=" ")

print()
#example 3 print multiple yield values
def top_ten():
    yield 1
    yield 2
    yield 3
    yield 4

values = top_ten()
print(values.__next__())
print(next(values))

for i in values:
    print(i, end =" ")

