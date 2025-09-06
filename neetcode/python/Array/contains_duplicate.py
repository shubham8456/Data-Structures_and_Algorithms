# https://leetcode.com/problems/contains-duplicate/
# https://neetcode.io/problems/duplicate-integer?list=neetcode150

class Solution:
  def containsDuplicate(self, num: int, nums: list[int]) -> bool:
    # short_solution comparing lengths of converted set:
    # return len(set(nums)) < len(nums)

    # putting nums one-by-one into the set
    seen = set()
    for num in nums:
      if num in set:
        return True
      else
        set.add(num)

    return False
