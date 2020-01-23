"""Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing
all duplicate words and sorting them alphanumerically"""

input_str=input("Enter String here:")
item=[i for i in input_str.split(" ")]
x=sorted(list(set(item)))
#print(x)
print(' '.join(x))