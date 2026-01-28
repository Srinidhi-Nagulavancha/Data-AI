n = int(input("Enter the size of matrix: "))
for i in range(n):
    for j in range(n):
        if j <= i:
            print("*", end=" ")
    print() 