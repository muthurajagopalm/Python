def mutate_string(string, position, character):
    str_list = list(s)
    for i in range (len(str_list)):
        str_list[position] = character
        #print(str_list)
        joint = ''.join(str_list)
        #print(joint)
    return  joint

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


    
