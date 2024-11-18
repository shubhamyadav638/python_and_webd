# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator program
while True:
    # Prompt the user for input
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    
    # Take user input
    choice = input("Enter your choice: ")
    
    if choice == "quit":
        break
    
    # Check if the choice is valid
    if choice not in ["add", "subtract", "multiply", "divide"]:
        print("Invalid input. Please try again.")
        continue
    
    # Prompt the user for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform the selected operation and display the result
    if choice == "add":
        print("Result: ", add(num1, num2))
    elif choice == "subtract":
        print("Result: ", subtract(num1, num2))
    elif choice == "multiply":
        print("Result: ", multiply(num1, num2))
    elif choice == "divide":
        result = divide(num1, num2)
        if result == "Cannot divide by zero":
            print(result)
        else:
            print("Result: ", result)
