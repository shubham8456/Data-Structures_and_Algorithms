from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
  i, j = 0, 0
  result = []

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  # result.extend(left[i:])
  # result.extend(right[j:])

  while i < len(left):
    result.append(left[i])
    i += 1

  while j < len(right):
    result.append(right[j])
    j += 1

  return result


def merge_sort(nums: List[int]) -> List[int]:
  if len(nums) <= 1:
    return nums

  mid = len(nums) // 2
  left  = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])

  return merge(left, right)
  


# Usage
arr = [3,6,4,7,2,6,7]
result = merge_sort(arr)
print(f"List: {arr} can be sorted to:{result}.")
