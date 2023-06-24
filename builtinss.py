from functools import reduce
from typing import List, Dict, Tuple, Any

# ! iter

colors: Tuple[str, str, str] = ("Red", "Green", "Blue")

colors_iter = iter(colors)

color1 = next(colors_iter)
color2 = next(colors_iter)
color3 = next(colors_iter)

print(color1, color2, color3)


# ^ Map

scores: List[int] = [10, 20, 30]
new_scores = map(lambda score: score * 2, scores)
# ! Returns iter so Converted to any type
new_scores: List[int] = list(new_scores)
print(new_scores)


# ^ Filter

marks: List[int] = [80, 90, 100, 75]
top_marks: List[int] = list(filter(lambda mark: mark >= 90, marks))
print(top_marks)

users_details: List[List[Any]] = [
    ["Akash", 18],
    ["Pugazh", 20],
    ["Virus", 12],
]
users_permitted: List[List[Any]] = list(
    filter(lambda user: user[1] >= 18, users_details)
)

print(users_permitted)

# ^ Reduce

natural_numbers_10: List[int] = [num for num in range(1, 11)]

sum_natural_numbers_10: int = reduce(lambda a, b: a + b, natural_numbers_10)

print(sum_natural_numbers_10)


stocks: Dict[str, int] = {
    "AAPL": 121,
    "AMZN": 3380,
    "MSFT": 219,
    "BIIB": 280,
    "QDEL": 266,
    "LVGO": 144,
}
new_stocks: Dict[str, int] = {key: value * 0.2 for (key, value) in stocks.items()}

print(new_stocks)
