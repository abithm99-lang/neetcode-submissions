class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Create an empty dictionary to hold our groups
        anagram_map = defaultdict(list)

        for s in strs:
            tempList = [0] * 26

            for char in s:
                tempList[ord(char)-ord("a")]+=1
            
            anagram_map[tuple(tempList)].append(s)

        return list(anagram_map.values())
        