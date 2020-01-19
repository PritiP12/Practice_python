#returns an integer the number of decimal places a number has
def count_dec_place(n):

    if "." not in n:
        return False
    else:
        len_n=n.split(".")
        return len(len_n[1])
count_dec_place('89.89567898')