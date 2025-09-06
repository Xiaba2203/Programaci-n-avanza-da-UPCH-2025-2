set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1 | set2
print(set1, set2, set3)   # {1, 2, 3} {3, 4, 5} {1, 2, 3, 4, 5}

set3 = set1 - set2
print(set1, set2, set3)   # {1, 2, 3} {3, 4, 5} {1, 2}

set3 = set1 & set2
print(set1, set2, set3)   # {1, 2, 3} {3, 4, 5} {3}

set3 = set1 ^ set2
print(set1, set2, set3)   # {1, 2, 3} {3, 4, 5} {1, 2, 4, 5}
