import collections

stu = collections.namedtuple('Entry', ['Name', 'Age', 'DOB'])
s1=stu('Vinod', 35, '25Aug')
print(s1)
s2=['Mithun', 45, '30Sep']
print(s2)
print(stu._make(s2))
s3=stu('Rachna', 25, '01Dec')
print(s3)






