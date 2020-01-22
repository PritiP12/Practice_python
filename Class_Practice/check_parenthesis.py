class Paranthisis:
    def check(self,str1):
        lst=[]
        pchar= {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                lst.append(parenthese)
            elif len(lst) == 0 or pchar[lst.pop()] != parenthese:
                return False
        return len(lst) == 0

x=Paranthisis()
print(x.check("(){}[]"))
print(x.check("[){]]]]"))

