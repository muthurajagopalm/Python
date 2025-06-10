

def cel_to_fahren(x):
    fahren = (c*1.8) + 32
    return fahren

c = float(input("Enter the Current Celcius in your location:"))
print(cel_to_fahren(c))
