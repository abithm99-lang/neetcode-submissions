class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numexist = set(nums)
        globalCounter = 0

        for num in nums:
            counter = 0
            tempNum = num
            while tempNum in numexist:
                tempNum-=1
            startofseq = tempNum+1
            while startofseq in numexist:
                counter+=1
                startofseq+=1
            globalCounter = max(globalCounter, counter)

        return globalCounter
        