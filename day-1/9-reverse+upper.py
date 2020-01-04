'''def reverse_capitalize(txt):
	return ''.join(reversed(txt.upper()))
print(reverse_capitalize("merge"))
'''
string1=input("Enter String:")
if string1.islower():
    string1=string1[::-1]
    print(string1.upper())
else:
    string1=string1[::-1]
    print(string1.lower())

#######Using Function#######
'''def reverse_capitalize(txt):
	return ''.join(reversed(txt.upper()))
print(reverse_capitalize("merge"))
'''