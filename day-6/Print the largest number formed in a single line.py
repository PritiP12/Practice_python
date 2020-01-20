# N,K

N, K = input("EnterN,EnterK:").split()
change = int(input("ENTER CHANGE NO:"))
N = list(N)
for i in range(int(K)):
    N[i] = change

print(''.join([str(i) for i in N]))



