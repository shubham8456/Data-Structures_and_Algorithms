from typing import List

def binary_search(arr: List[int], num: int, start: int, end: int) -> int:
  # base condition
  if start > end:
    return -1

  mid = start + (end - start) // 2

  # base condition
  if num == arr[mid]:
    return mid
  # recursive condition
  elif num < arr[mid]:
    return binary_search(arr, num, start, mid - 1)
  # recursive condition
  elif num > arr[mid]:
    return binary_search(arr, num, mid + 1, end)



# Usage
number = 5
arr = [0,1,2,3,4,5,6]
result = binary_search(arr, number, 0, len(arr) - 1)
print(f"The index at which the number '{number}' is found in the array -- {arr} -- is {result}.")
