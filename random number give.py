from random import*
def random_number():
    minimum = int(input("Enter the minimum number: "))
    maximum = int(input("Enter the maximum number: "))
    number =randint(minimum, maximum)
    print("Random number:", number)

random_number()