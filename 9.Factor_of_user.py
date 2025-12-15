#WAP to find factor of user input number using function

def find_factors(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

number = int(input("Enter a number: "))
result = find_factors(number)
print("Factors of", number, "are:", result)




