students = {"peter", "john"}
print(students)          # {'peter', 'john'}
students.add("john")
print(students)          # {'peter', 'john'} (no se duplica)
students.add("peterson")
print(students)          # {'peter', 'john', 'peterson'}
students.remove("peter")
print(students)          # {'john', 'peterson'}
