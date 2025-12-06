"""WAP to ask a student name, his mark in five different subjects(without loop), find his total marks,
  pass fail category and division. Full mark=100, pass=35"""
#using functions with argument

def total_marks(subject1, subject2, subject3, subject4, subject5):
    total = subject1 + subject2 + subject3 + subject4 + subject5
    return total

def pass_fail_category(total):
    if(subject1>=35 and subject2>=35 and subject3>=35 and subject4>=35 and subject5>=35):
        return "Pass"
    else:
        return "Fail"

def division(percent):
    if(subject1>=35 and subject2>=35 and subject3>=35 and subject4>=35 and subject5>=35):
     if percent >= 80 and percent <=100:
        return "Distinction"
     elif percent >= 70 and percent < 80:
        return "1st Division"
     elif percent >= 60 and percent < 70:
        return "2nd Division"
     elif percent >= 35 and percent < 60:
       return "Just Pass"
    else:
        return None

def calculate_percentage(total):
    percentage = (total / 500) * 100
    return percentage

def get_student_info():
    name = input("Enter Your Name: ")
    subject1 = float(input("Enter marks for Subject 1: "))
    subject2 = float(input("Enter marks for Subject 2: "))
    subject3 = float(input("Enter marks for Subject 3: "))
    subject4 = float(input("Enter marks for Subject 4: "))
    subject5 = float(input("Enter marks for Subject 5: "))
    return name, subject1, subject2, subject3, subject4, subject5

name, subject1, subject2, subject3, subject4, subject5 = get_student_info()

total = total_marks(subject1, subject2, subject3, subject4, subject5)
percentage = calculate_percentage(total)

print("Total Marks:", total)
print("Pass/Fail:", pass_fail_category(total))
print("Division:", division(percentage))
