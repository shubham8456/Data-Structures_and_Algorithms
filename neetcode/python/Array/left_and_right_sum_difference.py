# https://leetcode.com/problems/left-and-right-sum-differences/description/

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        left_sum = right_sum = 0
        left_sum_arr, right_sum_arr = [0] * nums_len, [0] * nums_len

        for i in range(nums_len):
            left_sum_arr[i] = left_sum
            right_sum_arr[nums_len-1-i] = right_sum
            left_sum  += nums[i]
            right_sum += nums[nums_len-1-i]
        
        result = []
        for i in range(nums_len):
          result.append(abs(left_sum_arr[i] - right_sum_arr[i]))
        
        return result


# Usage
list_1 = [10, 4, 8, 3]
result = Solution().leftRightDifference(list_1)
print(result)
