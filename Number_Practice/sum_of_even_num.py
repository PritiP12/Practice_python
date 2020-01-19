#takes two parameters (start, stop), and returns the sum of all even numbers in the range.
def sum_even_nums_in_range(start, stop):
    sum=0
    for i in range(start,stop+1):
        if(i%2)==0:
            sum=sum+i
    return sum
print(sum_even_nums_in_range(1, 6))