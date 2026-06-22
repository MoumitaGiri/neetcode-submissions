#O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {} # empty dictionary
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in preMap:
                return [preMap[diff], i]
            else:
                preMap[nums[i]] = i

#O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]         
        