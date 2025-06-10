from collections import Counter 

num_of_shoes = input("Enter the number of shoes:")
shoe_sizes = map(int, input().split())
shoes_sz_count = Counter(shoe_sizes)

earnings = 0
num_customers = int(input("Enter the customers:"))
for _ in range (num_customers):
    size, price = map(int, input().split())
    if shoes_sz_count[size] > 0:
        earnings += price
        #print(earnings)
        shoes_sz_count[size] -= 1
print(earnings)