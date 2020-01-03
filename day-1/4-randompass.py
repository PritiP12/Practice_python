import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input("Enter password length between 10-15:"))
p =  "".join(random.sample(s,passlen ))
print(p)














