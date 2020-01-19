#The digit distance between two numbers is the absolute value of the difference of each digit
def digit_distance(n1,n2):
    return sum(int(x) for x in str(n2-n1))
print(digit_distance(111, 790))