class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        if len(s)%2 != 0:
            return False 
        for i in s:
            if i in mapping:  # If it's a closing bracket
                if not stack or stack.pop() != mapping[i]:
                    return False
            else:  # It's an opening bracket
                stack.append(i)

        return not stack
