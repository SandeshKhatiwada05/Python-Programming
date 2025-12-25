# Binary Addition

def binary_converter(a, b):
    st = ""
    c = 0
    while a != 0 or b != 0:
        add_last_digit = a % 10 + b % 10 + c
        if add_last_digit == 1:
            st = str(1) + st
            c = 0
        elif add_last_digit == 0:
            st = str(0) + st
            c = 0
        elif add_last_digit == 2:
            st = str(0) + st
            c = 1
        elif add_last_digit == 3:
            st = str(1) + st
            c = 1
        a //= 10
        b //= 10
    if c == 1:
        st = str(1) + st
    print(st)

def main():
    a = int(input("Enter First Binary Number: "))
    b = int(input("Enter Second Binary Number: "))
    binary_converter(a, b)

main()
