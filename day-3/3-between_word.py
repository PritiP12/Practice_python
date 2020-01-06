'''
Write a function that takes three string arguments (first, last, word)
and returns true if (when alphabetically sorted) word is found between first and last.
'''
def is_between(first, last, word):
  return [first,word,last] == sorted([first,word,last])
print(is_between("apple", "banana", "azure"))