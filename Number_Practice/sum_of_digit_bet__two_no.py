#sums the total number of digits between two numbers

def sum_bet_num(n1,n2):
    result=0
    for i in range(n1,n2+1):
        result += sum([int(x) for x in str(i)])
    print(result)
sum_bet_num(19,22)