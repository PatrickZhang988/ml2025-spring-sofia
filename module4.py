# module4.py

# Step 1: ask for N
N = int(input("Enter a positive integer N: "))

# Step 2: read N numbers
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Step 3: ask for X
X = int(input("Enter the number to search for (X): "))

# Step 4: output result
if X in numbers:
    index = numbers.index(X) + 1  # 1-based index
    print(index)
else:
    print(-1)
