def fibanocci(n):
    a,b = 0,1
    result = []

    for _ in range (n):
        result.append(a)
        a,b = b, a+b
    return result
number = int(input("Enter the Fib number "))

print(fibanocci(number))
