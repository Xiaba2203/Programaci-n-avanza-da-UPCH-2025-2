s1 = {1, 4, 5, 6}
s2 = {1, 3, 6, 7}

print(s1.union(s2))              # {1, 3, 4, 5, 6, 7}
print(s1 | s2)                   # {1, 3, 4, 5, 6, 7}
print(s1.intersection(s2))       # {1, 6}
print(s1 & s2)                   # {1, 6}
print(s1.difference(s2))         # {4, 5}
print(s1 - s2)                   # {4, 5}
print(s1.symmetric_difference(s2)) # {3, 4, 5, 7}
print(s1 ^ s2)                   # {3, 4, 5, 7}
