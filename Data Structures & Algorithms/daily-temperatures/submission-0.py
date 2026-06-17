class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # 1 2
        res = [0]*len(temperatures) # 1
        maxVal = float('-inf') # 38

        for i,val in enumerate(temperatures):
            while stack and val>temperatures[stack[-1]]:
                remove = stack.pop()
                res[remove] = i-remove
            maxVal = max(maxVal,val)
            stack.append(i)
        return res
        
        [0, 1, 2,  3, 4, 5, 6]
        [30,38,30,36,35,40,28]