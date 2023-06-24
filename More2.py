from typing import List, Any

x: List[Any] = [1, 2, 3, 4]

print(x[1])
print(x[1:3])
print(len(x))
# ^ access with index or range of indexes
# ! Mutable

x[0] = "Akash"  # mutation in index or range
print(x)

x.insert(1, "Abi")  # ! .insert(index, value) Doesnot mutate add in 1st position
print(x)


# ! Add Items using Append Insert Extend
x.append(12)
x.insert(len(x), "HELLO")
x.extend(["NewListElement", "Varta mame durr"])
print(x)


# ! remove elements using remove pop clear del
x.pop()  # & also supports index in pop
print(x)
x.remove("Abi")  # & value specified to be deleted
print(x)
del x[len(x) - 1]  # & del deletes value or entire list
print(x)
x.clear()  # & empties the list
print(x)

# ! Looping for while for Comprehension

testList: List[Any] = ["Akash", "Pugazh", 18, "Btech"]

for ele in testList:
    print(ele)

index: int = 0
while index < len(testList):
    print(testList[index])
    index += 1

print("Comprehension looping")
[print(ele) for ele in testList]  # simplest way

# ! List Comprehension

print(testList)
new_list: List[Any] = [elements for elements in testList if elements != 18]
# & Comprehension way of list creation also add Conditions
print(new_list)

even_numbers_list: List[int] = [number for number in range(11) if number % 2 == 0]
print(even_numbers_list)

even_numbers_list.sort(reverse=True)
print(even_numbers_list)
even_numbers_list.reverse()
print(even_numbers_list)


# ! List Copying and Joining/ Merging

copy_even_numbers_list: List[int] = even_numbers_list.copy()
print(copy_even_numbers_list)

odd_numbers_list: List[int] = [number for number in range(11) if number % 2 != 0]
print(odd_numbers_list)

merge_even_odd_list: List[int] = even_numbers_list + odd_numbers_list
print(merge_even_odd_list)

range_10_list: List[int] = []
range_10_list.extend(merge_even_odd_list)
print(range_10_list)
