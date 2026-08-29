class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time : O(n * k log k)
        # Space : (n * k)
        d = defaultdict(list)

        for s in strs:
            k = ''.join(sorted(s))
            d[k].append(s)
        return list(d.values())