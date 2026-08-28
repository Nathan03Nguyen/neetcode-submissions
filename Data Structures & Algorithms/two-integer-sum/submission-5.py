class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time : O(n)
        # Space : O(n)
        d = {}

        for i, x in enumerate(nums):
            if (y := target - x) in d:
                return [d[y], i]
            d[x] = i