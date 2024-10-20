class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Stack to keep track of the characters in the expression
        stack = []
        
        # Iterate over each character in the expression
        for char in expression:
            if char == ')':  # When we reach a closing parenthesis
                # We will evaluate the current sub-expression
                sub_expr = []
                
                # Pop characters until we find the opening parenthesis '('
                while stack and stack[-1] != '(':
                    sub_expr.append(stack.pop())
                
                # Pop the opening parenthesis '('
                stack.pop()
                
                # The next character in the stack is the operator
                operator = stack.pop()
                
                # Evaluate the sub-expression based on the operator
                if operator == '&':
                    stack.append('t' if all(c == 't' for c in sub_expr) else 'f')
                elif operator == '|':
                    stack.append('t' if any(c == 't' for c in sub_expr) else 'f')
                elif operator == '!':
                    # For the NOT operator, it only applies to one element
                    stack.append('t' if sub_expr[0] == 'f' else 'f')
            elif char != ',':
                # Push everything else (except commas) onto the stack
                stack.append(char)
        
        # The result is the last element left in the stack
        return stack.pop() == 't'
