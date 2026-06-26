class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        longest = 0 
        n = len(s)
        count = [0] * 26

        for r in range(n):
            count[ord(s[r]) - 65] += 1

            while(((r-l+1) - max(count)) > k):
                count[ord(s[l]) - 65] -=1
                l +=1

            longest = max((r - l + 1), longest)

        return longest

if __name__ == "__main__":
    s = "XYYX"
    k = 2
    sol = Solution()
    print(sol.characterReplacement(s, k))
        