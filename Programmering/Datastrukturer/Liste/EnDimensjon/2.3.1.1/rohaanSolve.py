def summarize(list):
    if type(list) != "list":
        return
    
    sum = 0

    for i in range(len(list)):
        sum += list[i]
    
    return sum


list = [1, 5, 5, 7, 2, 2345, 2456, 2345]

print(summarize(list))