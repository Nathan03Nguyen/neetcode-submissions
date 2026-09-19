class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = cur_min = 1

        for n in nums:
            temp = cur_max * n
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(temp, cur_min * n, n)
            res = max(cur_max, res)
        return res