"""WAP to ask the user to enter 1,2,3,4,5 . If he enters 1 ask the user to enter name and reverse that 
string. If 2 ask the user to put height of 3 persons and find the shortest one. If 3 ask a user to
check if it is prime composite or prime. If 4 ask the user to enter any string if it is palyndrom or
not using using recusrsive function.If 5 then Tower of Honoi. If  6 display thankyou message and exit.
If user inputs any othervalue with is invalid(such as string) ask to enter valid choice again"""

def reverse_string():
    name = input("Enter a name: ")
    reversed_name = name[::-1]
    print("Reversed name:", reversed_name)


def find_shortest_height():
    heights = []
    for i in range(3):
        while True:
            try:
                height = int(input("Enter height of person {}: ".format(i+1)))
                heights.append(height)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    shortest_height = min(heights)
    print("Shortest height:", shortest_height)


def check_prime():
    while True:
        try:
            num = int(input("Enter a number: "))
            if num < 2:
                print("Neither prime nor composite.")
            else:
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print("Prime")
                else:
                    print("Composite")
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")


def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


def palindrome_check():
    while True:
        string = input("Enter a string: ")
        if all(char.isdigit() for char in string):
            print("Invalid input. Please enter a string.")
        else:
            break
    if is_palindrome(string):
        print("Palindrome")
    else:
        print("Not a palindrome")


def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)


while True:
    try:
        choice = int(input("Enter a choice (1-6): "))
        if choice == 1:
            reverse_string()
        elif choice == 2:
            find_shortest_height()
        elif choice == 3:
            check_prime()
        elif choice == 4:
            palindrome_check()
        elif choice == 5:
            num_disks = int(input("Enter the number of disks: "))
            tower_of_hanoi(num_disks, 'A', 'B', 'C')
        elif choice == 6:
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid choice (1-6).")
    except ValueError:
        print("Invalid input. Please enter an integer choice.")
