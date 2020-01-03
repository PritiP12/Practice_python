def sentence(s):
    sen=s.split()
    for i in range (len(sen)):
        if len(sen[i]) > 4:
            sen[i]='*'*len(sen[i])
    return ' '.join(sen)
print(sentence("Create a function that takes in a string and outputs the string "
               "but with words over four characters to be censored with *"))

#using list comphresion
'''
:return ''.join(["*"*len(i) if len(i)>4 else i for i in s.split()])
'''

