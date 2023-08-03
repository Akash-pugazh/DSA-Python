def RecursiveNumber(n):
    if n < 1:
        print(f"End of n : {n}")
    else:
        print(f"Progressing n : {n}")
        RecursiveNumber(n - 1)


RecursiveNumber(10)
