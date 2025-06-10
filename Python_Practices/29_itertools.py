from itertools import chain
from itertools import count
from itertools import repeat

'''for i in count(10,2):
    print(i, end=' ')
    if i > 20:
        break'''

'''count = 0
for item in repeat("Muthu",3):
    print(item) '''  

list_1 = [1,10,3,4,5]
list_2 = [5,6,7,8,9]

listAll = tuple(chain(list_1, list_2))
print(listAll)