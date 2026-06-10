class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainList=[]
        for i,string in enumerate(strs):
            tempList=[]
            tempList.append(string)
            for idx,val in enumerate(strs):
                if idx == i or len(string)!=len(val):
                    continue
                sorted_str = "".join(sorted(val))
                sorted_str_curr = "".join(sorted(string))
                if sorted_str_curr==sorted_str:
                    tempList.append(val)
            tempList.sort()
            mainList.append(tempList)
        unique_tuples = set(tuple(inner) for inner in mainList)

        return [list(inner) for inner in unique_tuples]
          