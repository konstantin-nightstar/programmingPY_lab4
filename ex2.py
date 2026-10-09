"""Exercise 2: print each requested figure for a positive integer n."""

for i in range(0, 5):
    for j in range(5 - i):
        print("*", end=" ")
    print()
print()

for i in range(0, 5):
    for j in range(i + 1):
        print("*", end=" ")
    print()
print()

for i in range(0, 5):
    for j in range(0, 5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Write your solutions below.