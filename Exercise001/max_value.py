#Find maximum int value from list which contain both str and int python

lst=['Hello',10,2,"Hi","Bye",5,3,6.9]
print(max([i for i in lst if isinstance(i, int)]))

#output:10