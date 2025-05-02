
marks = [[70, 86, 90],[61, 75, 85],[50, 65, 78]]

for i in range(3):
    total = sum(marks[i])
    average = round(total / 3,2)
    print(f"Student {i + 1} - Total: {total} , Average: {average:.2f}")

