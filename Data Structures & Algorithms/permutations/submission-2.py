class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time : O(n!)
        # Space : O(n)
        res, sol = [], []

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return res