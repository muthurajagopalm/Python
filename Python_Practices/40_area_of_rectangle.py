
###########   Key word arguments   ############
'''def area_of_rectangle(length,width,a,d):
    area = length * width
    return area

areaa = area_of_rectangle(length = 5, width=2, d =2, a=3)
print(areaa)'''

############ Default Arguments      ################

def area_of_rectangle(length, width=5):
    area = length * width
    return area

areaa  =  area_of_rectangle(5)
print(areaa)