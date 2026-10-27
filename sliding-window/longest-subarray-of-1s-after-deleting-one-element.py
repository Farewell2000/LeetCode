class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        start = 0
        result = 0
        count = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                count += 1
            
            while count > 1:
                while nums[start] != 0:
                    start += 1
                count -= 1
                start += 1
            
            result = max(end - start, result)
        
        return result