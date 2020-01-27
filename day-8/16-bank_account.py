#Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
#D 100
#W 200
t=int(input("Enter number of transactions ? "))
balance=0
while t!=0:

    t_input,amount=input("Enter Input (D/W)? amount?").split()
    amount=int(amount)
    if t_input=="D":
        balance += amount
    elif t_input=="W":
        balance -= amount
    t-=1

print("Total Balance:",balance)

