class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        hm = defaultdict(list)

        for i in range(len(nums)):
            hm[nums[i]].append([nums[i], i])

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                sum = -1 * (nums[i] + nums[j])
                if sum in hm:
                    for subseq in hm[sum]:
                        if subseq[1] == i or subseq[1] == j:
                            continue
                        tup = tuple(sorted([nums[i], nums[j], subseq[0]]))
                        res.add(tup)
        
        return [list(tup) for tup in res]