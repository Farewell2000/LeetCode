class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0

        while s_pointer < len(s):
            while t_pointer < len(t) and t[t_pointer] != s[s_pointer]:
                t_pointer += 1
            if t_pointer >= len(t):
                return False
            else:
                t_pointer += 1
                s_pointer += 1
            
        return True