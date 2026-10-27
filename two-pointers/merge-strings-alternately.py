class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        wordCombine = ""
        if len(word1) == len(word2):
            wordLength = len(word1)
            for i in range(wordLength):
                wordCombine += word1[i]
                wordCombine += word2[i]
            return wordCombine
        else:
            if len(word1) > len(word2):
                wordLength = len(word2) 
            else:
                wordLength = len(word1)
            for i in range(wordLength):
                wordCombine += word1[i]
                wordCombine += word2[i]
            if len(word1) > len(word2):
                wordCombine += word1[wordLength:] 
            else:
                wordCombine += word2[wordLength:] 
            return wordCombine