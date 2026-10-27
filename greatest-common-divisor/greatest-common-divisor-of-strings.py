class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        for i in range(min(len(str1), len(str2)), 0, -1):
            x = str1[0:i]
            if len(str1) % len(x) == 0 and len(str2) % len(x) == 0 and x * (len(str1) // len(x)) == str1 and x * (len(str2) // len(x)) == str2:
                return x
        return ""

