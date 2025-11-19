# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")

    choice = input("Choose 1, 2 or 3: ")

    if choice == "1":
        print("Result:", add(x, y))
    elif choice == "2":
        print("Result:", subtract(x, y))
    elif choice == "3":
        print("Result:", multiply(x, y))
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
