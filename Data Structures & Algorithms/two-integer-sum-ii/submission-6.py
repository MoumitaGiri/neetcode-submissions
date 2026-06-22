class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while(left<right):
            totalSum = numbers[left] + numbers[right]
            if(totalSum>target):
                right -=1
            elif(totalSum<target):
                left +=1
            else:
                return[left+1, right+1]

if __name__ =="__main__":
    numbers = [1,2,3,4]
    target = 3
    obj = Solution()
    result = obj.twoSum(numbers, target)
        