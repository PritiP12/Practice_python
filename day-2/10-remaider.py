def mystery_func1(lst, n):
    return [x % n for x in lst]
print(mystery_func1([5, 4, 6, 9], 2))