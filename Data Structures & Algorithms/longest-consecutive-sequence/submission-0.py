class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_length = 0
        visited_value = {num: False for num in nums}

        for val in nums:

            next_value = val + 1
            current_value = 1

            while next_value in visited_value and not visited_value[next_value]:
                
                current_value += 1
                visited_value[next_value] = True
                next_value += 1

            prev_value = val -1  

            while prev_value in visited_value and not visited_value[prev_value]:
                
                current_value +=1
                visited_value[prev_value] = True
                prev_value -= 1

            longest_length = max(current_value, longest_length)     
        return longest_length

   