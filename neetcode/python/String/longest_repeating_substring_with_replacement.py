# https://neetcode.io/problems/longest-repeating-substring-with-replacement?list=blind75

# from typing import Dict

# class Solution:
#   def characterReplacement(self, s: str, k: int) -> int:
#     left = 0
#     result = 0
#     freq_map = {}

#     for right in range(len(s)):
#       highest_freq = self.update_char_freq_and_get_highest_freq(freq_map, s[right])
#       length_of_curr_substring = right - left + 1

#       if (length_of_curr_substring - highest_freq) <= k:
#         result = max(result, length_of_curr_substring)
#       else:
#         freq_map[s[left]] = freq_map.get(s[left], 0) - 1
#         left += 1

#     return result


#   def update_char_freq_and_get_highest_freq(self, freq_map: Dict[str, int], s: str) -> int:
#     freq_map[s] = freq_map.get(s, 0) + 1

#     freq_arr = []
#     for char in freq_map.keys():
#       freq_arr.append([freq_map[char], char])
#     freq_arr.sort()

#     return freq_arr[-1][0]


class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    left = 0
    result = 0
    freq_map = {}

    for right in range(len(s)):
        freq_map[s[right]] = 1 + freq_map.get(s[right], 0)

        if (right - left + 1) - max(freq_map.values()) > k:
            freq_map[s[left]] -= 1
            left += 1
        
        result = max(result, right - left + 1)

    return result



string = 'AABABBA'
k = 1
result = Solution().characterReplacement(string, k)
print(result)
