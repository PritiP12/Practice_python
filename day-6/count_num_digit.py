input_str=input("Enter here:")
count=0
prev=0
for x in input_str:
    if x.isdigit() and not prev.isdigit():
        count += 1
    prev=x
print(count)
