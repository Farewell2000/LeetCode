class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        start = 0
        end = 0
        count = 0
        result = 0

        while end < len(nums):
            if nums[end] == 0:
                count += 1
            end += 1

            if count > k:
                while start < len(nums) and nums[start] != 0:
                    start += 1
                start += 1
                count -= 1
            
            if end - start > result:
                result = end - start
        
        return result
