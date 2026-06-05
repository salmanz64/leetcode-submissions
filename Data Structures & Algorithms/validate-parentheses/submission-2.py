class Solution:
    def isValid(self, s: str) -> bool:
        para = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        stack = []

        for char in s:
            if char not in para:
                stack.append(char)
            else:
                if not stack or stack.pop() != para[char]:
                    return False
        return len(stack) == 0




        

        