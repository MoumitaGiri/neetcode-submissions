class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1

        while l<r:
            totalSum = numbers[l] + numbers[r]
            if(totalSum>target):
                r -=1
            elif(totalSum<target):
                l +=1
            else:
                return[l+1, r+1]

if __name__ == "__main__":
    numbers = [1,2,3,4]
    target = 3
    obj = Solution()
    result =  obj.twoSum(numbers, target)

        