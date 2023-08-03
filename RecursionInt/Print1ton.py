def print1ton(n):
    if n > 1:
        print1ton(n - 1)
    print(n)
print1ton(10)