#O(n)
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        pallindromeSet = ''

        for i in s:  #Alphanumeric characters consist of letters check whether alphanumeric
            if(i.isalnum()):
                pallindromeSet += i

        pallindromeSet = pallindromeSet.lower() #consider all as lower character

        if (pallindromeSet == pallindromeSet[::-1]):
            return True
        else:
            return False
#O(n)
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        checkPalindrome = ''

        for i in s:
            if i.isalnum():
                checkPalindrome += i.lower()
        return checkPalindrome == checkPalindrome[::-1]

#Time & Space Complexity
#Time complexity: O(n)
#Space complexity: O(n)

#O(n) AscII two pointer l for left pointer and r is right pointer

class Solution:
    def isPalindrome(self, s : str):
        l,r = 0 , len(s) - 1

        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while r > l and not self.alphanum(s[r]):
                r -= 1
            if s[r].lower() != s[l].lower():
                return False
            l, r = l+1, r-1
        return True

    def alphanum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))

#Time & Space Complexity
#Time complexity: O(n)
#Space complexity: O(1)






