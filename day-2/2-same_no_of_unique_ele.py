def same(a1,a2):
    if len(set(a1))==len(set(a2)):
        print('True')
    else:
        print('False')
same([3,1,3],[1,2])