#number and email match pattern
import re
str1="91-80-87611-243"
str2="xyz@gmail.com"

#for Number
pattern1=("\w{2}-\w{2}-\w{5}-\w{3}")#{/+[0-9]{2}-[0-9]{2}-[0-9]{5}-[0-9]{3}}
if (re.search(pattern1,str1)):
    print("True")
else:
    print("False")

#for email:
pattern2="\w+@\w+.com"
if (re.search(pattern2,str2)):
    print('true')
else:
    print('false')
