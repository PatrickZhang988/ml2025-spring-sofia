from module5_mod import NumberManager

def main():
    manager = NumberManager()

    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N > 0:
                break
            else:
                print("N must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(N):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                manager.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    while True:
        try:
            X = int(input("Enter a number to search: "))
            result = manager.search_number(X)
            print(result)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
