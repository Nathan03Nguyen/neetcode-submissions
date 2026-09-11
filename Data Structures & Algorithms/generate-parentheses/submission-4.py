class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openn, close, sol, n):
            if openn == n and close == n:
                res.append(''.join(sol))
                return
            
            if openn < n:
                sol.append('(')
                backtrack(openn + 1, close, sol, n)
                sol.pop()
        
            if openn > close:
                sol.append(')')
                backtrack(openn, close + 1, sol, n)
                sol.pop()
        backtrack(0, 0, [], n)
        return res