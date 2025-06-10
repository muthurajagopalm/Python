my_list = ["a", "b", "c", "d", "a", "b"]
'''list_dict = dict.fromkeys(my_list)
print(list_dict)

list_again = list(list_dict)
print(list_again)'''


def listfunc(x):
    return list(dict.fromkeys(x))
    
print(listfunc(my_list))
