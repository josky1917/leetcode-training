class Solution:
    def isValid(self, s):
        parentheses_map = {"(": ")","[": "]","{": "}"}
        left = ["(","[","{"]
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            elif stack and i == parentheses_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
parenthese = Solution()
s = "(){}{{{}[]}}"
bool = parenthese.isValid(s)
print(bool)