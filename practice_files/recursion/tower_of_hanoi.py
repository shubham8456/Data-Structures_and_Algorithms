# Problem 6 at:
# https://algocademy.com/blog/10-best-coding-exercises-for-mastering-recursion-from-beginner-to-advanced/
# https://www.geeksforgeeks.org/dsa/c-program-for-tower-of-hanoi/

def tower_of_hanoi(number_of_rings: int, tower_1: str, tower_2: str, tower_3: str) -> None:
  # base condition
  if number_of_rings == 0:
    return

  # recursive condition
  tower_of_hanoi(number_of_rings - 1, tower_1, tower_3, tower_2)
  print(f"Move {number_of_rings} ring(s) from Tower {tower_1} to Tower {tower_3}.")
  tower_of_hanoi(number_of_rings - 1, tower_2, tower_1, tower_3)


# Usage
number_of_rings = 3

tower_of_hanoi(number_of_rings, 'A', 'B', 'C')
