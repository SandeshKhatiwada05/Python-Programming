#Bubble shot
#WAP to enter 10 diff num and find max and min without minimum and maximum function

numbers = []
for i in range(10):
    num = int(input("Enter number {}: ".format(i+1)))
    numbers.append(num)

min_num = numbers[0]
max_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print("Minimum number: ", min_num)
print("Maximum number: ", max_num)
