class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        [-1, 0, 1,2,3]

        left_product=[1] * n
        right_product=[1] * n

        prefix = 1
        for i in range(n):
            left_product[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            right_product[i] = suffix
            suffix = suffix * nums[i]

        res = [left_product[i] * right_product[i] for i in range(n)]

        return res

        