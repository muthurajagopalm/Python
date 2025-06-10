import cmath


z = complex(input())

polar_coordinates = cmath.polar(z)

#join = ' '.join(map(str, polar_coordinates))

print(polar_coordinates[0])
print(polar_coordinates[1])