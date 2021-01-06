import random
import string

n, m = eval(input("input the number of lists and the limit of the elements for every list\n"))
source = string.digits + string.ascii_letters
mylist = [[''.join(random.sample(source, random.randint(1, m)))] for i in range(n)]
print(sorted(mylist, key = lambda x:len(x[0]), reverse = True))