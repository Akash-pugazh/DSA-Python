for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print("\n")

n = 6
for i in range(1, n):
    for j in range(n - i):
        print("*", end=" ")
    print("\n")


for i in range(1, 5):
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

for i in range(1, 5):
    for j in range(i - 1):
        print(" ", end=" ")
    for k in range(5 - i):
        print("*", end=" ")
    print()

n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()


for i in range(n + 1):
    for j in range(i + 1):
        print(chr(97 + j), end=" ")
    print()


n = 4
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for _ in range(2 * i + 1):
        print("*", end=" ")
    for j in range(n - i - 1):
        print(" ", end=" ")
    print()

