import string
import random

sourse = string.digits + string.ascii_letters + string.punctuation
mylist = [random.choice(sourse) for i in range(1000)]
mystring = ''.join(mylist)
d = dict()
for mychar in mystring:
    d[mychar] = d.get(mychar, 0) + 1
for i, j in d.items():
    print(i, j, "times")