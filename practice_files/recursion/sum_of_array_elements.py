from typing import List

def sum_of(nums: List[int]) -> int:
  # base condition
  if len(nums) == 0:
    return 0
  # recursive condition
  return nums[0] + sum_of(nums[1:])


# Usage
arr = [1,2,3,4,5]
result = sum_of(arr)
print(f"The sum of elements in the array, {arr}, is {result}.")
