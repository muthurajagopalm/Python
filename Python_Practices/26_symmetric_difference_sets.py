   
set_a = input()
set_anums = set(map(int, input().split()))

set_b = input()
set_bnums = set(map(int, input().split()))


sym_diff = set_anums.symmetric_difference(set_bnums)
print(sym_diff)

for num in sorted(sym_diff):
    print(num)