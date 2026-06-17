class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = []
        stack = []
        for i in range(len(position)):
            array.append([position[i],speed[i],(target-position[i])/speed[i]])
        array.sort(reverse=True)


        for i in array:
            stack.append(i[2])
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            

