a_list = list(eval(input("input a integer list\n")))
print("original list:", a_list)
b_list = sorted(a_list, reverse = True)
c_list = [a_list[i] for i in range(0, len(a_list), 2)]
print("reversed list:", b_list)
print("even positions list:", c_list)