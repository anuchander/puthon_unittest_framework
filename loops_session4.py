#example 1
list1=["BMW", 'Mercedes', "Toyota", "Honda"]
for i in list1:
    print(i, end=" ")
print()

#example 2
for i in range(10):
    if (i==5):
       #continue
        pass # pass does nothing but provides code for indent block
        #break # if for loop does not completed fully, else condition for for not executed
    print(i,end=" ")
else:
    print()
    print("For loop completed")

#example 3
i=0
while(i<5):
    if(i==3):
        break
    print(i, end=" ")
    i+=1
else:
    print()
    print("While loop completed!")

print()
#example 4
for i in range(5):
    for j in range(5):
        print(i,j, end=" ")
    print()