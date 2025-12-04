def total():
    print("Enter marks of 5 subjects")
    print("Enter your mark")
    dsa = float(input("DSA:              "))
    stat = float(input("Statistics:       "))
    nm = float(input("Numerical Method: "))
    cg = float(input("Graphics:         "))
    ca = float(input("CA:               "))
    total = dsa + stat + nm + cg + ca
    print("Your total is", total)
    if dsa < 35 or stat < 35 or nm < 35 or cg < 35 or ca < 35:
        print(name, "you're", "Fail!!")
    else:
        print("You Passed")
    return total

def percent():
    a = total()
    per = (a / 500) * 100
    print("Your percentage is", per, "%")
    return per

def div():
    per = percent()
    if per >= 50:
        if per >= 80 and per < 100:
            print("Distinction")
        elif per >= 70 and per < 80:
            print("1st Division")
        elif per >= 60 and per < 70:
            print("2nd Division")
        else:
            print("Just Pass")
    else:
        print(None)

name = input("Enter Your Name: ")
div()
