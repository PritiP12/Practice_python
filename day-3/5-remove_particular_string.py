'''
Create a function which returns the word in the string, but with all the fog letters removed.
 However, if the string is clear from fog, return "It's a clear day!".
'''
def clearFog(txt):
	fogless = ''.join(i for i in txt if i not in 'fog')
	return "It's a clear day!" if fogless == txt else fogless
print(clearFog('fogfogfffoooofftreesggfoogfog') )