from typing import List


# def left_product(current_index: int, nums: List[int]) -> int:
#     value = 1
#     if current_index == 0:
#         return value
#     else:
#         value = nums[0]
#         temp_index = 1
#         while temp_index != current_index:
#             value *= nums[temp_index]
#             temp_index += 1
#         return value


# def right_product(current_index: int, nums: List[int]) -> int:
#     value = 1
#     if current_index == (len(nums) - 1):
#         return value
#     else:
#         value = nums[current_index + 1]
#         temp_index = current_index + 1
#         while temp_index != (len(nums) - 1):
#             temp_index += 1
#             value *= nums[temp_index]
#         return value


if __name__ == "__main__":
    nums: List[int] = [-1, 1, 0, -3, 3]

    result: List[int] = [1] * len(nums)

    prefix: int = 1
    for _ in range(len(nums)):
        result[_] = prefix
        prefix *= nums[_]

    postfix: int = 1
    for _ in range(len(nums) - 1, -1, -1):
        result[_] *= postfix
        postfix *= nums[_]

    print(result)

    # result: List[int] = []

    # def leftProduct(current_index: int, nums: List[int]) -> int:
    #     value = nums[0]
    #     temp_index = 1
    #     while temp_index != current_index:
    #         value *= nums[temp_index]
    #         temp_index += 1
    #     return value

    # def rightProduct(current_index: int, nums: List[int]) -> int:
    #     temp_index = current_index + 1
    #     value = nums[temp_index]
    #     while temp_index != (len(nums) - 1):
    #         temp_index += 1
    #         value *= nums[temp_index]
    #     return value

    # # ~ Prefix

    # for _ in range(len(nums)):
    #     if _ == 0:
    #         result.append(1)
    #     else:
    #         pr: int = leftProduct(current_index=_, nums=nums)
    #         result.append(pr)

    # # ~ Postfix with producting the existing values

    # for _ in range(len(nums) - 1, -1, -1):
    #     if _ == len(nums) - 1:
    #         result[len(result) - 1] *= 1
    #     else:
    #         result[_] *= rightProduct(current_index=_, nums=nums)

    # print(result)

    # for index, num in enumerate(nums):
    # print(f"INDEX : {index}")
    # l_product: int = left_product(current_index=index, nums=nums)
    # r_product: int = right_product(current_index=index, nums=nums)
    # print(f"LEFT : {l_product} RIGHT : {r_product}")
    # result.append(l_product * r_product)
    # print(result)
