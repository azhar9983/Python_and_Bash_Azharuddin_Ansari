'''
#1. Grade Checker
Take a score as input and print the grade based on the following:
90+ : “A”
80–89 : “B”
70–79 : “C”
60–69 : “D”
Below 60 : “F”
Use a basic if / else statement to determine the grade.
'''

def grade_checker(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = float(input("Enter the score: "))
grade = grade_checker(score)
print(f"The grade for the score {score} is: {grade}")

