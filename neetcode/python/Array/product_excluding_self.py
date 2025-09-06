# https://leetcode.com/problems/product-of-array-except-self
# https://neetcode.io/problems/products-of-array-discluding-self?list=blind75

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                zeroCount += 1
                if zeroCount > 1:
                    return [0] * len(nums)

        res = []
        for num in nums:
            if zeroCount == 1:
                res.append(product if num == 0 else 0)
            else:
                res.append(int(product/num))
        return res
