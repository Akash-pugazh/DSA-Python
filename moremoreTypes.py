from typing import Dict, Set, Any, FrozenSet

# ! Dictionaries -> Ordered Changeable NotAllowDuplicates

my_dict: Dict[str, Any] = {
    "Name": "Akash",
    "Age": 12,
    "Age": 18,
}


print(my_dict["Name"])
print(my_dict["Age"], len(my_dict))
name: str = my_dict.get("Name")
print(name)
my_dict_keys = my_dict.keys()
my_dict_values = my_dict.values()
print(my_dict_keys, my_dict_values)
my_dict_items = my_dict.items()
print(my_dict_items)

for key, value in my_dict.items():
    print(key, ":", value)


test_set: Set[str] = {"Java", "C", "Python"}
frozen_test_set: FrozenSet[str] = frozenset(test_set)
print(frozen_test_set)
for index, value in enumerate(frozen_test_set, start=1):
    print(f"{index} : {value}")


s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

unique_elements = s1.symmetric_difference(s2)
print(unique_elements)
