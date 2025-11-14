#TASK-1: Build a Calculator CLI App
# Define functions for each mathematical operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error: Cannot take modulus by zero!"
    return a % b


# Function to display the menu
def print_menu():
    print("\n=== Simple CLI Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("0. Exit")


# Main program
def main():
    history = []  # optional: to store results

    while True:
        print_menu()
        choice = input("Enter your choice (0-6): ").strip()

        if choice == "0":
            print("✅ Exiting the calculator. Thankyou!")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    result = add(a, b)
                    operation = f"{a} + {b} = {result}"
                elif choice == "2":
                    result = subtract(a, b)
                    operation = f"{a} - {b} = {result}"
                elif choice == "3":
                    result = multiply(a, b)
                    operation = f"{a} * {b} = {result}"
                elif choice == "4":
                    result = divide(a, b)
                    operation = f"{a} / {b} = {result}"
                elif choice == "5":
                    result = power(a, b)
                    operation = f"{a} ** {b} = {result}"
                elif choice == "6":
                    result = modulus(a, b)
                    operation = f"{a} % {b} = {result}"

                print(f"Result: {result}")
                history.append(operation)

            except ValueError:
                print("❌ Invalid input. Please enter numeric values.")

        elif choice == "7":
            if not history:
                print("No calculations yet.")
            else:
                print("\n📜 Calculation History:")
                for item in history:
                    print(item)

        else:
            print("❌ Invalid choice! Please choose between 0–6.")


# Run the main function
if __name__ == "__main__":
    main()