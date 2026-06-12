class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        stack = []

        for char in s:

            if char in ["[", "{", "("]:
                stack.append(char)
            else:
                letter = stack.pop() if stack else ""
                if letter != mapping[char]:
                    return False
        
        return not stack