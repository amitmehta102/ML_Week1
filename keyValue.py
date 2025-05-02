students = {29: "Akash", 34: "Aman", 38: "Amit"}
def search(roll):
    print(students.get(roll, "Student not found."))
search(int(input("Enter roll number: ")))

