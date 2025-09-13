# https://leetcode.com/problems/valid-parentheses
# https://neetcode.io/problems/validate-parentheses?list=neetcode150

# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 != 0:
#             return False

#         opening_brackets = ['(', '{', '[']
#         closing_brackets = [')', '}', ']']
#         stack = []
#         for char in s:
#             if char in opening_brackets:
#                 stack.append(char)
#             elif char in closing_brackets:
#                 if len(stack) == 0:
#                     return False
#                 else:
#                     top_item = stack.pop()
#                     if top_item != self.complement_of(char):
#                         return False
#         return True if len(stack) == 0 else False


#     def complement_of(self, char: str) -> str:
#         char_map = {
#             ')': '(',
#             '}': '{',
#             ']': '['
#         }
#         return char_map[char]

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
