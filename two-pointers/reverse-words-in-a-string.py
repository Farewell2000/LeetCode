class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        word = []
        result = []
        while i <= len(s):
            if i < len(s) and s[i] != " ":
                word.append(s[i])
            else:
                if word != []: result.append("".join(word))
                word = []
            i += 1
        result.reverse()
        return " ".join(result)