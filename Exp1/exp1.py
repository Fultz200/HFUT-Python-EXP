import random
ans = random.randint(1, 10)
count = 0
flag = 0    # if guess is right, it's 1, 0 otherwise
print("now guess a number between 1 and 10")

for count in range(3):
    x = int(input())
    if x == ans:
        count += 1
        flag = 1
        break
    elif x < ans:
        print("too small")
        count += 1
    elif x > ans:
        print("too large")
        count += 1

if flag == 1:
    print("right")
else:
    print("you have no chance anymore.")
    print("the answer is ", ans)
