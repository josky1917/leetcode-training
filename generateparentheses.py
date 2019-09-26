class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrack(s = "", left = 0, right = 0):
            if left ==n and right == n:
                res.append(s)
            if left < n:
                backtrack(s+"(", left+1, right)
            if left > right:
                backtrack(s+")", left, right+1)
        backtrack()
        return res