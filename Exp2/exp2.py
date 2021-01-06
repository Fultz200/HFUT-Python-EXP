setA = set(eval(input("input set a separated by commas\n")))
setB = set(eval(input("input set b separated by commas\n")))
print("intersection{}\nunion{}\ncomplement{}\n".format(setA & setB, setA | setB, setA - setB))