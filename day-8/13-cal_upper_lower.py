#a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

sentence=input("Enter Sentence here:")
cnt1=0
cnt2=0

for i in sentence:
    if i.isupper():
        cnt1 += 1
    elif i.islower():
        cnt2 += 1
    else:
        pass
print("UPPER:",cnt1)
print("LOWER:",cnt2)
