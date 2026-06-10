class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorted_list =[]
        hm = {}
        for num in nums:
             hm[num] = hm.get(num,0)+1
    
        sorted_list = sorted(hm.keys(), key=hm.get, reverse=True)
        return sorted_list[:k]