class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        end = k
        result = 0

        vowels = "aeiou"

        for letter in s[:end]:
            if letter in vowels:
                result += 1

        count = result
        start += 1
        end += 1

        while end <= len(s):
            if s[end-1] in vowels and s[start-1] not in vowels:
                count += 1
            elif s[end-1] not in vowels and s[start-1] in vowels:
                count -= 1

            if count > result: 
                result = count
            
            start += 1
            end += 1
        
        return result
            