#Reverse a string using recursive function

def reverse_string(input_str):
    if len(input_str) == 0:
        return input_str
    else:
        return reverse_string(input_str[1:]) + input_str[0]

# Example usage
string = "Hello, World!"
reversed_string = reverse_string(string)
print(reversed_string)
