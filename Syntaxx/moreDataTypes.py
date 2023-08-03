from typing import Tuple, Set

# & Tuples Dictionary Set

test_tuple: Tuple[int, int] = (12, 32)  #! Unchangeable Ordered AllowDuplicates
# test_tuple[1] = 122 #! Error

print(test_tuple, f" \nLength Test Tuple : {len(test_tuple)}")

#! Add Comma after one item to create tuple with one item -> ("apple", )


print(12 in test_tuple)

# !  Convert To list and perform operations
# ~ Add - append() Remove - remove() del

x1 = list(test_tuple)
x1.append(500)
test_tuple = tuple(x1)
print(test_tuple)

# ~ Unpacking Tuple

(width, *whole_numbers, height) = (200, 1, 2, 3, 4, 5, 400)

print(width, height)
print(whole_numbers)
# ~ Similar loooping as List


# & SET

test_set: Set[int] = {12, 212, 12}
print(test_set)  # ! No  Duplicates Unchangeable Unordered


# ! add() update() -> Update takes not only set but also the iterables like tuples list set and it *** updaates previous set ***

test_set.add(321)
print(test_set)

temp_set: Set[int] = {23, 312, 543, 65}
test_set.update(temp_set)
print(test_set)

# ! remove() - false->error discard() ->false- noerror

test_set.remove(321)
print(test_set)


# ! Return new set With two sets -> union

test_set_updated = test_set.union(test_tuple)
print(test_set_updated)

# ! intersecrion_update

x = {12, 32, 43}
y = {12, 32, 33312, 14}
# x.intersection_update(y)
# print(x)
# z = x.intersection(y)
# print(z)
# x.symmetric_difference_update(y)
# print(x)
z = x.symmetric_difference(y)
print(z)
