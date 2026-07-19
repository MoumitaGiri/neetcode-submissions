class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority = nums[0]
        vote = 1
        n = len(nums)

        for i in range(1,n):
            if vote == 0:
                vote +=1
                majority = nums[i]
            elif majority == nums[i]:
                vote +=1
            else:
                vote -=1

        return majority
        