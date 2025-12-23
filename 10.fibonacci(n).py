#1 1 2 3 5.... 13th term
#WAP to add odd sum and even sum from 1 to 20
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n+1):
            a, b = b, a + b
        return b

n = 13
result = fibonacci(n)
print("The", n, "term of the sequence is:", result)
