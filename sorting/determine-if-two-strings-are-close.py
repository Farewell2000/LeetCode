class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1map = {}
        word2map = {}

        for letter in word1:
            if letter in word1map:
                word1map[letter] += 1
            else:
                word1map[letter] = 1

        for letter in word2:
            if letter in word2map:
                word2map[letter] += 1
            else:
                word2map[letter] = 1
                
        word1key = list(word1map.keys())
        word2key = list(word2map.keys())
        word1value = list(word1map.values())
        word2value = list(word2map.values())

        if len(word1key) != len(word2key) or len(word1value) != len(word2value):
            return False
        else:
            word1key.sort()
            word2key.sort()
            word1value.sort()
            word2value.sort()
            for i in range(len(word1key)):
                if word1key[i] != word2key[i]:
                    return False
            for i in range(len(word1value)):
                if word1value[i] != word2value[i]:
                    return False    

        return True