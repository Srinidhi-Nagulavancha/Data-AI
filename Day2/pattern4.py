n = int(input("Enter the size of matrix: "))

for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()