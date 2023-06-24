from typing import List

x: int = 12

y: str = str(x)
# ^ Casting

z: bool = True
a: int = int(z)


my_string: str = "Hello World"
print(my_string[:])
print(my_string[2:])
print(my_string[:4])
print(my_string[::-1])
# ~ Slicing

# ^ String Methods

print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())
print(my_string.strip())
print(my_string.replace("l", "ewww"))
print(my_string.find("e"))
print(my_string.split())

test: List[str] = ["Hello", "World"]

