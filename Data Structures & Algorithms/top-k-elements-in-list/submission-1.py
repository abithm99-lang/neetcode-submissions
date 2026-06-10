class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorted_list =[]
        # hm = {}
        # for num in nums:
        #      hm[num] = hm.get(num,0)+1
    
        # sorted_list = sorted(hm.keys(), key=hm.get, reverse=True)
        # return sorted_list[:k]
        hm={}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
             hm[num]=hm.get(num,0)+1
        
        for key,val in hm.items():
            freq[val].append(key)
        res=[]

        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
        return []