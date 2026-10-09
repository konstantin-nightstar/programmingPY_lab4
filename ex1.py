"""Exercise 1: display the two requested number series."""


for i in range(10):
    for j in range(10):
        print(f"({i},{j})", end=" ")
    print()
print()
for i in range(10):
    for j in range(10):
        print(i * 10 + j, end=" ")
    print()
# Write your solution below.