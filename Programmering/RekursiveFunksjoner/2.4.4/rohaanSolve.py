def pascal(row, place):
    if (row == place or place == 0):
        return 1
    else:
        return pascal(row - 1, place) + pascal(row - 1, place -1)

print(pascal(4, 2))