# takes two numbers as input (num, length) and returns a list of multiples of num up to length.
#input
#num:2
#length:5
#output
#[2, 4, 6, 8, 10]

num=int(input("num:"))
length=int(input("length:"))
lst=[]
i=1
while i <= length:
    lst.append(i*num)
    i += 1
print(lst)
