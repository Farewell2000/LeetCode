class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        small = 0
        large = len(nums) - 1
        result = 0

        while small < large and small < len(nums) - 1 and large > 0:
            if nums[small] + nums[large] == k:
                result += 1
                small += 1
                large -= 1
            
            elif nums[small] + nums[large] < k:
                small += 1
            
            else: large -= 1
        
        return result