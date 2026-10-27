class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right :
            water = (right - left) * min(height[left], height[right])

            if water > result:
                result = water

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return result