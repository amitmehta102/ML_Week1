temperatures = []

for i in range(5):
    temp=float(input(f"Enter the temperature of the day{i+1}:"))
    temperatures.append(temp)

average = sum(temperatures)/5
print(f"\nThe temperatures you entered are:{temperatures}")
print(f"The Average temperature over 5 days is: {average:.2f}degrees")