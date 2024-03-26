# 1. The Calculator App

# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.


def add(number1, number2):
    solution = number1 + number2
    print(solution)

def sub(number1, number2):
    solution = number1 - number2
    print(solution)

def mul(number1, number2):
    solution = number1 * number2
    print(solution)

def div(number1, number2):
    solution = number1 / number2
    print(solution)

def choose():
    option = input("Choose an operation(add, subtract, multiply, divide):")
    number1 = int(input("Enter first number:"))
    number2 = int(input("Enter second number:"))
    if option == "add":
        try:
            add(number1, number2)
        except:
            pass
    if option == "subtract":
        try:
            sub(number1, number2)
        except:
            pass
    if option == "multiply":
        try:
            mul(number1, number2)
        except:
            pass
    if option == "divide":
        try:
            div(number1, number2)
        except ZeroDivisionError:
            print("You can't divide by zero silly")
choose()

# 2. The Shopping List Maker
my_list= []
def add_books():
    while True:
      book = input("Add book to your list:")
      if book == "quit":
          break
      my_list.append(book)
add_books()
def show_list():
    print("Here's your list of books: ")
    for list in my_list:
        print(list)
def removing():
    while True:
        user_input = input("What would you like to remove? Type 'next' to move on. ")
        if user_input == "next":
            break
        my_list.remove(user_input)
removing()
show_list()


# 3. The Grade Analyzer

# Task 1: Code a function to calculate the average grade.
grades = [98, 67, 85, 56, 95, 88, 73, 69, 77, 50]
def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total

def grades_average(grades):
    return grades_sum(grades) / float(len(grades))

print(grades_average(grades))

# Task 2: Implement a function to find the highest and lowest grade.
def hi_lo(grades):
    highest = max(grades)
    lowest = min(grades)
    return [lowest, highest]
print(hi_lo(grades)) 

# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
grade = int(input("Enter grade here: "))
if grade >= 90:
    print("Your grade is an A")
elif grade >= 80:
    print("Your grade is a B")
elif grade >= 70:
    print("Your grade is a C")
elif grade >= 60:
    print("Your grade is a D")
else:
    print("Your grade is an F")