class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1]

        for i in range(1, n):
            result.append(result[i-1] * nums[i-1])
        
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix *= nums[i]
        
        return result