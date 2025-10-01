# https://leetcode.com/problems/3sum/
# https://neetcode.io/problems/three-integer-sum?list=

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combos = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values for the first number

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    combos.append([nums[i], nums[left], nums[right]])
                    left  += 1
                    right -= 1

                    # Skip duplicates
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return combos


nums = [-1,0,1,2,-1,-4]
result = Solution().threeSum(nums)
print(result)
