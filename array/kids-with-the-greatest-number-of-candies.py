class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                result.append(True)
            else: result.append(False)
        return result
