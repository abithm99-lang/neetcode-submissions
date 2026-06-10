class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Create an empty dictionary to hold our groups
        anagram_map = {}
        
        for string in strs:
            # 2. How do we find the "signature"? 
            # Hint: "".join(sorted(string)) gives you a sorted string
            sorted_str = "".join(sorted(string))
            
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = [string]
            else:
                anagram_map[sorted_str].append(string)
            
        # 5. Return just the values of the dictionary as a list
        return list(anagram_map.values())