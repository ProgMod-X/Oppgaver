
def sum(tall):
    sum = 0
    for i in range(len(tall)):
        sum += tall[i]
        # Debugging
        # print("tall:", tall[i], "\t\tsum:", sum)
    return sum

tall = [1, 2, 3, 4, 5]

print(sum(tall))