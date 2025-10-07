def fibonacci(num: int) -> int:
  if num in [0,1]:
    return num
  
  return fibonacci(num - 1) + fibonacci(num - 2)


# Usage
position = 6
result = fibonacci(position)
print(f"The {position}th number in the fibonacci sequence is {result}.")
