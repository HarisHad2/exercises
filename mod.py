def is_even(x):
    return x % 2 == 0

def evens(my_list):
    res = []
    for x in my_list:
        if is_even(x):
            res.append(x)
    return res




my_list = [1,2,4,5,13,35,36,8]
yyy = evens(my_list)
print(yyy)
#print(is_even(1))
