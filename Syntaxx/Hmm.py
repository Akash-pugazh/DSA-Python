from typing import Union

x: int = 0

if x is None:
    print("None")
elif x > -1:
    print("Postive")
else:
    print("Negative")


message: str = "It's Zero" if x == 12 else "It's not Zero"
#  ~ Ternary Operator
print(message)


_temp: int = 0
while _temp <= 5:
    if _temp == 2:
        _temp += 1
        continue
    print(_temp)
    _temp += 1


# ~ * Args
def test_function(*numbers: int) -> str:
    res: int = 0
    for num in numbers:
        res += num
    return f"Sum of {numbers} : {res}"


print(test_function(1, 2, 3))

# ~ Keyword Args


def test_func(number1: int, number2: int) -> int:
    return number1 + number2


print(test_func(number2=10, number1=20))


# * lambda Functions

add_two_numbers = lambda x, y: x + y
print(add_two_numbers(10, 20))


number = Union[int, float]


def sum_two_numbers(x: number, y: number) -> number:
    return x + y
