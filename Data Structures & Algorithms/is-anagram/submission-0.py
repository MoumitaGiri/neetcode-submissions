class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_Count_s = {}
        char_Count_t = {}

        for i in range(len(s)):
            char_Count_s[s[i]] = char_Count_s.get(s[i], 0) + 1
            char_Count_t[t[i]] = char_Count_t.get(t[i], 0) + 1

        return char_Count_s == char_Count_t


#O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_Count_s = {}

        for char in s:
            char_Count_s[s[char]] = char_Count_s.get(s[char], 0) + 1

        for char in t:
            if char not in char_Count_s or char_Count_s[char] == 0:
                return False
            else:
                char_Count_s[char] -=1
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)



        


        