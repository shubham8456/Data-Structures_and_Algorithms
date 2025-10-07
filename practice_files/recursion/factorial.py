def factorial(num: int) -> int:
  # base condition
  if num in [0,1]:
    return 1
  
  # recursive condition
  return num * factorial(num - 1)


# Usage
number = 6
result = factorial(number)
print(f"Factorial of number {number} is {result}.")
