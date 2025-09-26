# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# https://neetcode.io/problems/longest-substring-without-duplicates?list=blind75

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    longest_substring = 0
    char_set = set()

    for right in range(len(s)):
      while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
      char_set.add(s[right])
      longest_substring = max(longest_substring, right - left + 1)

    return longest_substring
