class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = cur_min = 1

        for n in nums:
            temp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(temp, n * cur_min, n)
            res = max(cur_max, res)
        return res