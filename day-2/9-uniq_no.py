def return_unique(lst):
	return list(filter(lambda x: lst.count(x) < 2, lst))
print(return_unique([1,2,3,4,8,9,2,1,3,2]))