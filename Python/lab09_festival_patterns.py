n = int(input("Enter the number of rows: "))

print("Pattern 1: Star Triangle")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPattern 2: Number Triangle")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPattern 3: Inverted Star Triangle")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPattern 4: Pyramid")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
