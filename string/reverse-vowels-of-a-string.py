class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        chars = list(s)
        end_pointer = len(chars) - 1
        start_pointer = 0
        while start_pointer < end_pointer:
            if chars[start_pointer] not in vowels:
                start_pointer += 1
            elif chars[end_pointer] not in vowels:
                end_pointer -= 1
            else:
                chars[start_pointer], chars[end_pointer] = (chars[end_pointer], chars[start_pointer])
                start_pointer += 1
                end_pointer -= 1
        return "".join(chars)
            



