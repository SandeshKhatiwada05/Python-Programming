# Input 12 numbers
numbers = []
for i in range(12):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Remove duplicates using a dictionary
unique_numbers = list(dict.fromkeys(numbers))

# Display the unique numbers
print("Unique numbers:", unique_numbers)
