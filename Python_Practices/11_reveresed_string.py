names = "Hello"
i = len(names)-1
rev_string = ""
#print(i)
while i >= 0 :
    rev_string += names[i]
    #print(rev_string)
    i-=1
print(rev_string)
