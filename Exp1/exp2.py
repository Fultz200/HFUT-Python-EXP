import random
ans = random.randint(1, 10)
count = 0
flag = 0
print("now guess a number between 1 and 10")

while flag == 0:
    x = int(input())
    if x == ans:
        count += 1
        flag = 1
        break
    elif x < ans:
        count += 1
        print("too small")
    elif x > ans:
        count += 1
        print("too large")

if flag == 1:
    print("right")
else:
    print("you have no chance anymore")
    print("the answer is ", ans)