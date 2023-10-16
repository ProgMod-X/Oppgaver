def pascal(row, place):
    
    if place == 0 or place == row:
        return 1
    else:
        return (pascal(row - 1, place - 1) + pascal(row - 1, place))
    
    
print(pascal(3, 1))