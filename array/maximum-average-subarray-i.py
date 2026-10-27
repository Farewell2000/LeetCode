class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        start = 0
        end = k - 1

        average = sum(nums[start : end+1]) / k
        result = average

        if k == len(nums):
            return result
        else:
            for i in range(k, len(nums)):
                start += 1
                end += 1

                average -= (nums[start-1] - nums[end]) / k

                if average > result:
                    result = average
        
        return result