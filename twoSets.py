all_students = {"Amit", "Akash", "Aman", "Rohit", "Anand", "Ankit"}
football = {"Rohit", "Anand","Aman"}
cricket = {"Ankit", "Aman", "Amit","Rohit"}

print("Both:", football & cricket)
print("Only one:", football ^ cricket)
print("Neither:", all_students - (football | cricket))

