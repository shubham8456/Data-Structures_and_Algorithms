# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

from typing import Dict
import heapq

class Solution:
    def maxFreqSum(self, s: str) -> int:
        if len(s) == 0:
            return 0

        vowel_freq_map, consonant_freq_map = {}, {}
        for c in s:
            if self.is_vowel(c):
                vowel_freq_map[c] = vowel_freq_map.get(c, 0) + 1
            else:
                consonant_freq_map[c] = consonant_freq_map.get(c, 0) + 1

        return self.max_count(vowel_freq_map) + self.max_count(consonant_freq_map)


    def max_count(self, freq_map: Dict) -> int:
        if not freq_map:
            return 0

        heap = []
        for key in freq_map.keys():
            heapq.heappush(heap, [freq_map[key], key])

            if len(heap) > 1:
                heapq.heappop(heap)

        return heapq.heappop(heap)[0]


    def is_vowel(self, c: str) -> bool:
        return c in ['a', 'e', 'i', 'o', 'u']


# Usage
input_string = "aeiaeia"
result = Solution().maxFreqSum(input_string)
print(result)

