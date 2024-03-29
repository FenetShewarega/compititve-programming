class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i, j = 0, len(piles)-1
        ans = 0
        while i+2 <= j:
            ans += piles[j-1]
            i += 1
            j -= 2
            
        return ans