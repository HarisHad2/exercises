def divisble_by_7(yyy):
    
    for i in range(1, 1001):
        if i % 7 == 0 and i % 2 != 0:
            yyy.append(i)
    return yyy 
yyy = []

print(divisble_by_7(yyy))