def minst(num):
    if num[0] < num[1]:
        return num[0]
    else:
        return num[1]

def stoerst(num):
    if num[0] > num[1]:
        return num[0]
    else:
        return num[1]

num = [8, 3]

print("Minst: ", minst(num))
print("Størst: ", stoerst(num))
