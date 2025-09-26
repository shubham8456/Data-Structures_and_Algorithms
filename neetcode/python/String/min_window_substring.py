# https://leetcode.com/problems/minimum-window-substring/description/
# https://neetcode.io/problems/minimum-window-with-characters?list=blind75

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    char_count_map = {}
    for char in t:
      char_count_map[char] = 1 + char_count_map.get(char, 0)

    result = ""
    left = 0
    for right in range(len(s)):
      while s[right] not in char_count_map




s,t = "OUZODYXAZV", "XYZ"
expected_output = "YXAZ"
results = Solution().minWindow(s, t)
print(results == expected_output)
