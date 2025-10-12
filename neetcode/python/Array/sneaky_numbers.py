# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                result.append(nums[i])
            if len(result) == 2:
                break

        return result


# Usage
nums_1 = [7,1,5,4,3,4,6,0,9,5,8,2]
nums_2 = [0,3,2,1,3,2]
nums_3 = [0,1,1,0]
result = Solution().getSneakyNumbers(nums_2)
print(result)
