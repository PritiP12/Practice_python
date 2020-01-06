def check_no(lst):
    even_lst=[]
    odd_lst=[]
    for i in lst:
        if i%2==0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    print([even_lst,odd_lst])
check_no([1,8,9,7,5,6,4,2,3])

