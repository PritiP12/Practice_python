#Create a function that removes the first and last characters from a string.
def remove_first_last(txt):
    if len(txt) <2:
        print(txt)      #For words with two or fewer letters (including an empty string), return the string itself
    else:
        print(txt[1:-1])
remove_first_last("Hello")
remove_first_last("H")
remove_first_last('6')