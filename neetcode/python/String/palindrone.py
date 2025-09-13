# https://leetcode.com/problems/valid-palindrome
# https://neetcode.io/problems/is-palindrome?list=blind75

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(filter(str.isalnum, s.lower().strip()))

        l, r = 0, len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
