#WAP to print all the vowels in any word
"""WAP to find the frequency of vowels in any setence. Print the output  as following
   A---->
   E---->
   I---->
   O---->
   U---->"""

sentence = input("Enter Sentence: ")
check= sentence.upper()
print("Easier method answer")
print("A----->",check.count("A"))
print("E----->",check.count("E"))
print("I----->",check.count("I"))
print("O----->",check.count("O"))
print("U----->",check.count("U"))

#Same with for loop
print("\nSame result but with for loop")
vowels = "AEIOUaeiou"
freq = [0] * 5       #list [0,0,0,0,0]
for char in sentence:
    if char in vowels:
        if char == 'A' or char == 'a':
            freq[0] += 1
        elif char == 'E' or char == 'e':
            freq[1] += 1
        elif char == 'I' or char == 'i':
            freq[2] += 1
        elif char == 'O' or char == 'o':
            freq[3] += 1
        elif char == 'U' or char == 'u':
            freq[4] += 1

print("A---->", freq[0])
print("E---->", freq[1])
print("I---->", freq[2])
print("O---->", freq[3])
print("U---->", freq[4])

