class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numexist = set(nums)
        globalCounter = 0

        for num in nums:
            counter = 0
            if num-1 not in numexist:
                while (num+counter) in numexist:
                    counter+=1
            globalCounter = max(globalCounter,counter)

        return globalCounter
        