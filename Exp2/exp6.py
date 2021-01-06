import string

mylist = input("input a article\n")
mylist = mylist.replace(',', ' ').replace('.', ' ')
mylist = mylist.split()
myset = set(mylist)
mydict = {}
for i in myset:
    count = mylist.count(i)
    mydict[i] = count
for i, j in mydict.items():
    print(i, j, 'times')