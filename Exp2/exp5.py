import random

n, m = eval(input("input the number of integers and the limit of every integer\n"))
mytuple = tuple(random.randrange(1, m, 2) for i in range(n))
print(mytuple)