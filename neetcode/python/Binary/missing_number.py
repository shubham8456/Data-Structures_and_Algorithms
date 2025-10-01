# https://leetcode.com/problems/missing-number/description/
# https://neetcode.io/problems/missing-number?list=blind75

# O(n^2) time complexity, because of "i in nums" inside loop
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             if i not in nums:
#                 return i
#         return len(nums)

# O(n) using XOR
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         result = len(nums)
#         for i in range(len(nums)):
#             result ^= i ^ nums[i]
#         return result

# O(n) using Gauss Formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n+1)//2 - sum(nums)
