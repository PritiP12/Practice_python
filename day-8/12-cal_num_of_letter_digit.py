#accepts a sentence and calculate the number of letters and digits

sentence=input("Enter Sentence:")
result1=0
result2=0
for i in sentence:
    if i.isdigit():
        result1 += 1

    elif i.isalpha():
        result2 += 1

    else:
        pass
print("DIGIT:",result1)
print("LETTER:",result2)

