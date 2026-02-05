number = int(input("Enter an integer: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("The first number is larger")
elif num2 > num1:
    print("The second number is larger")
else:
    print("The numbers are equal")


score = int(input("Enter the exam score (0-100): "))
if score < 60:
    grade = 'F'
elif score < 70:
    grade = 'D'
elif score < 80:
    grade = 'C'
elif score < 90:
    grade = 'B'
else:
    grade = 'A'
print("Grade:", grade)


age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")