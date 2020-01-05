def wumbo(words):
    x="".join([i if i != 'M' else 'W' for i in words])
    return x
print(wumbo("I LOVE MAKING CHALLENGES"))
# return words.replace("M","W")