# counts the number of times a specific digit occurs in a range
def digit_occurrences(start, end, digit):
    count = 0
    for i in range(start, end + 1):
        count += str(i).count(str(digit))
    return count
print(digit_occurrences(51, 55, 5))