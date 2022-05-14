from queue import Queue
import queue

#list
list1 = [3,4,5]
list1.append(6)
print(list1)
print(list1.pop())
print(list1)

#queue - FIFO opertation
#the item which you entered first will be removed first
qu = Queue()
qu.put(5)
qu.put(6)
qu.put(7)
print(list(qu.queue))
print(qu.get())
print(list(qu.queue))

#queue - LIFO operation
#the item which you entered last will be removed first
q = queue.LifoQueue()
q.put(8)
q.put(9)
q.put(10)
print(list(q.queue))
print(q.get())
print(list(q.queue))


