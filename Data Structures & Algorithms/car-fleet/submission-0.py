class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time : O(n log n)
        # Space : O(n)
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pairs)[::-1]: #Reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)