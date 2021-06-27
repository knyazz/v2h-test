# You are given a list of stock prices in chronological order.
# Each element represents a price on a given day.
# Return the smallest missing positive integer
# for a given unsorted list of integers.
from typing import List


def smallest_missing_positive_int(nums: List[int] = None) -> int:
    nums = nums or list()

    m: int = max(nums)
    # all values in array are negative
    if m < 1:
        return 1

    # if one element in array
    if len(nums) == 1:
        # If it contains only one element
        return 2 if nums[0] == 1 else 1

    l: int = [0] * m
    for i in range(len(nums)):
        if nums[i] > 0:
            if l[nums[i] - 1] != 1:
                # Changing the value status at the index of our list
                l[nums[i] - 1] = 1

    for i in range(len(l)):
        # Encountering first 0, i.e, the element with least value
        if l[i] == 0:
            return i + 1
            # In case all values are filled between 1 and m
    return i + 2


if __name__ == '__main__':
    for nums in (
        [1, 2, 0],
        [3, 4, -1, 1],
        [7, 8, 9, 11, 12],
        [0, 10, 2, -9, -6],
        [10, 1, 2, -3, -4],
        [10, -3, -4, 0, 1],
        [10, -3, -4, 0, 2],
        [10, -3, -4, 0, 3, 2, 1],
    ):
        res = smallest_missing_positive_int(nums)
        print(f"result is {res} for {nums}")
