def main():
    try:
        
        number = int(input("Enter a number to see its multiplication table: "))
        
        
        for i in range(1, 10+1):
            print(f"{number} * {i} = {number * i}")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()


