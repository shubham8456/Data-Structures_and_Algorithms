# https://leetcode.com/problems/valid-parentheses
# https://neetcode.io/problems/validate-parentheses?list=neetcode150

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        bracket_map = {
          ')': '(',
          '}': '{',
          ']': '['
        }
        stack = []

        for char in s:
            if char in bracket_map.values():  # opening bracket
                stack.append(char)
            elif char in bracket_map:         # closing bracket
                if not stack or stack.pop() != bracket_map[char]:
                    return False

        return not stack
