student1 = {"peter", "john", "tim"}
student2 = {"peter", "johnson", "tim"}

print(student1.issuperset({"john"}))   # True
print(student1.issubset(student2))     # False
print({1, 2, 3} > {1, 2, 4})           # False
print({1, 2, 3} < {1, 2, 4})           # False
print({1, 2} < {1, 2, 4})              # True
print({1, 2} <= {1, 2, 4})             # True
