#BF: O(n^2)
# class Solution1:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if(nums[i] == nums[j]):
#                     return True
#         return False

#Sorting: O(nlogn)
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if(nums[i] == nums[i-1]):
#                 return True
#         return False

#HashSet: O(n), in hashset searching and adding time complexity is O(1)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueElements = set() #hashSet time complexity O(1)
        for n in nums: #going through the array list
            if n in uniqueElements: #array element present in unique hashset or not, O(1)
                return True
            else:
                uniqueElements.add(n) #this adding space is O(1)
        return False
        



