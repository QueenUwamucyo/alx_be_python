def main():
    try:
       
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
       
        operation = input("Choose the operation (+, -, *, /): ").strip()
        
        
        match operation:
            case '+':
                result = num1 + num2
                print(f"The result is {result}.")
            case '-':
                result = num1 - num2
                print(f"The result is {result}.")
            case '*':
                result = num1 * num2
                print(f"The result is {result}.")
            case '/':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result is {result}.")
                else:
                    print("Cannot divide by zero.")
            case _:
                print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
