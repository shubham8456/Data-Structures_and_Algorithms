# https://leetcode.com/problems/valid-anagram
# https://neetcode.io/problems/is-anagram?list=blind75

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq_dict, t_freq_dict = {}, {}

        for i in range(len(s)):
            s_freq_dict[s[i]] = s_freq_dict.get(s[i], 0) + 1;
            t_freq_dict[t[i]] = t_freq_dict.get(t[i], 0) + 1;

        return s_freq_dict == t_freq_dict
