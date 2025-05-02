
students = [(29, "Akash", 20),(34, "Aman", 21),(38, "Amit", 22)]


print("Student Information:\n")
print(f"{'Roll No.':<10} {'Name':<10} {'Age':<5}")
print("-" * 27)
for student in students:
    roll, name, age = student
    print(f"{roll:<10} {name:<10} {age:<5}")

