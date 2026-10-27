class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        result = dict()

        for num in arr:
            if num not in result:
                result[num] = 1
            else:
                result[num] += 1
        seen = set()

        for value in result.values():
            if value in seen:
                return False
            else:
                seen.add(value)
        
        return True