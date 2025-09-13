# https://leetcode.com/problems/3sum/
# https://neetcode.io/problems/three-integer-sum?list=

from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         combos = []
#         for first_num_idx, num_1 in enumerate(nums):
#             if first_num_idx > 0 and num_1 == nums[first_num_idx - 1]:
#                 continue  # Skip duplicate first numbers

#             target = -1 * num_1
#             i, j = first_num_idx + 1, len(nums) - 1

#             while i < j:
#                 sum_latter_two_nos = nums[i] + nums[j]
#                 if target == sum_latter_two_nos:
#                     combos.append([num_1, nums[i], nums[j]])

#                     # Skip duplicate nums[i]
#                     while i < j and nums[i] == nums[i + 1]:
#                         i += 1
#                     # Skip duplicate nums[j]
#                     while i < j and nums[j] == nums[j - 1]:
#                         j -= 1

#                     i += 1
#                     j -= 1

#                 elif target > sum_latter_two_nos:
#                     i += 1
#                 elif target < sum_latter_two_nos:
#                     j -= 1

#         return combos



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
