
# https://leetcode.com/problems/top-k-frequent-elements
# https://neetcode.io/problems/top-k-elements-in-list?list=blind75

# O(n logn) time complexity where n is the numbers in the list
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        arr = []
        for num in count.keys():
            arr.append([count[num], num])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        
        return res


# O(n logk) time complexity where n is the numbers in the list
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, [count[num], num])
            if (len(heap) > k):
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
