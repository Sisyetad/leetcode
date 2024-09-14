class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for dir in logs:
            if dir == "../":
                if stack:
                    stack.pop()
            elif dir != "./":
                stack.append(dir)
        print(stack)
        return len(stack)
