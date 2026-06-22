#O(n*k*log(k))
# class Solution1:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram = {}

#         for word in strs:
#             sorted_word = "".join(sorted(word))

#             if sorted_word in anagram:
#                 anagram[sorted_word].append(word)
#             else:
#                 anagram[sorted_word] = [word]

#         return list(anagram.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for word in strs:
            count = [0] * 26
            for char in word:

                count[ord(char) - ord('a')] +=1

            key = tuple(count)
            if key not in anagram:
                anagram[key] = [word]
            
            else:
                anagram[key].append(word)
        return list(anagram.values())
