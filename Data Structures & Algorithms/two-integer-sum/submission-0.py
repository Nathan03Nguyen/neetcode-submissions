class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for i, x in enumerate(nums):
            if (y := target - x) in ht:
                return [ht[y], i]
            ht[x] = i