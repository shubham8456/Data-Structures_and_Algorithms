# https://leetcode.com/problems/group-anagrams
# https://neetcode.io/problems/anagram-groups?list=blind75

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in str_map:
                str_map[sorted_string].append(string)
            else:
                str_map[sorted_string] = [string]

        return list(str_map.values())
