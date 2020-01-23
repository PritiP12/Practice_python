#a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

str_input=input("Enter string with comma-separated:")
value=[x for x in str_input.split(",")]
value.sort()
print(' '.join(value))
