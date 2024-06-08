def add(a, b):
    return a + b

# Main function to take input from user and perform addition
def main():
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    result = add(a, b)
    print(f"{a} + {b} = {result}")

if __name__ == "__main__":
    main()

