#A perfect number is a number that can be written as the sum of its factors, excluding the number itself.
#For example, 6 is a perfect number, since 1 + 2 + 3 = 6, where 1, 2, and 3 are all factors of 6.
# Similarly, 28 is a perfect number, since 1 + 2 + 4 + 7 + 14 = 28

num=int(input("Enter number to check weather is perfect or not:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(num,"is perfect")
else:
    print(num,"not perfect")
