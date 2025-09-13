from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr

arr = [234,436,43,2,1,345]
res = bubble_sort(arr)
print(res)
