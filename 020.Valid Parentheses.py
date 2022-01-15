class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    tmp = stack.pop()
                    if char == ')':
                        if tmp != '(':
                            return False
                    if char == ']':
                        if tmp != '[':
                            return False
                    if char == '}':
                        if tmp != '{':
                            return False

        if len(stack) == 0:
            return True
        return False
