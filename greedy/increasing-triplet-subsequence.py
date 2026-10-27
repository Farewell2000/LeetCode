class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = 2 ** 31 
        second = 2 ** 31

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False