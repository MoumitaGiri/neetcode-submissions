class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxiLength = 0
        right = 0
        left = 0
        my_dict = {}
        n = len(s)

        while right < n:
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1)

            maxiLength = max(maxiLength, right - left + 1)
            my_dict[s[right]] = right
            right += 1

        return maxiLength

if __name__ == "__main__":
    s = "zxyzxyz"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
        
        