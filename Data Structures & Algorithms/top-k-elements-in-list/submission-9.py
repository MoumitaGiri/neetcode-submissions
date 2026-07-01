from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict(Counter(nums))
        
        bucket = [[] for _ in range(len(nums)+1)]

    
        for val,freq in count.items():
            bucket[freq].append(val)
            
        
        n = len(bucket) - 1
        result = []
        for freq in range(n,-1, -1):
            result.extend(bucket[freq])
            if len(result) == k:
                return result
    
    
if __name__ == "__main__":
    nums = [1,2,2,3,3,3]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))
    
        