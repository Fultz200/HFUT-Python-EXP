import math
import random


def fibonacci(n):
    """show the number smaller than n in Fibonacci sequence"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        (a, b) = (b, a + b)


def primernumber(n):
    if n <= 2:
        print("the number should be larger than 2")
    else:
        result = []
        number = 2
        for number in range(2, n):
            divisor = 2
            for divisor in range(2, int(math.sqrt(number) + 1)):
                if number % divisor == 0:
                    break
            result.append(number)
        print(result)


def ispalindrome(mystr):
    if type(mystr) != str:
        print("it's not a string at all")
    else:
        if mystr == mystr[::-1]:
            print(mystr, "yes")
        else:
            print(mystr, "no")


def getatuple(n):
    a_list = list(random.choice(range(1,10)) for i in range(0, n))
    print("the list is:", a_list)
    average = sum(a_list) / len(a_list)
    a_tuple = tuple(str(average))
    b_tuple = tuple([j for i, j in enumerate(a_list) if j > average])
    c_tuple = a_tuple + b_tuple
    return c_tuple


def getworkeffect(dayup):
    level = 1.00
    daydown = 0.01
    for i in range(365):
        if i % 7 == [0, 6]:
            level *= 1 - daydown
        else:
            level *= 1 + dayup
    return level


def getdayupvalue():
    dayup = 0.01
    while getworkeffect(dayup) < 37.78:
        dayup += 0.01
    print("the dayup value should be ", dayup)


def splice(str1, str2):
    length1 = len(str1)
    length = min(length1, len(str2))
    k = max(range(0, length+1), key=lambda i: i if str1[length1-i:] == str2[:i]else False)
    return str1+str2[k:]


print("Fibonacci test")
fibonacci(25)
print("primer number test")
primernumber(25)
print("palindrome test")
ispalindrome("abcdcba")
ispalindrome("asdfghj")
print("list test")
getatuple(6)
print("work effect test")
getdayupvalue()
print("lambda test")
splice("1234", "34567")