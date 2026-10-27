class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        prefix = 0

        for delta in gain:
            prefix += delta
            altitude = max(altitude, prefix)
        
        return altitude