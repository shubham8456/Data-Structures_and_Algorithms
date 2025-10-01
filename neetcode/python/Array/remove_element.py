# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return right + 1

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         # Use a 'write' pointer to place non-val elements at the start
#         write = 0
#         for read in range(len(nums)):
#             if nums[read] != val:
#                 nums[write] = nums[read]
#                 write += 1
#         return write
