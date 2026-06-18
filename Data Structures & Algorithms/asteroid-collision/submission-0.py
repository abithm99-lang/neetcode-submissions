class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            destroyed = False
            while stack and  (stack[-1] > 0 and ast < 0):
                if stack[-1] > abs(ast):
                    destroyed = True
                    break
                elif stack[-1] == abs(ast):
                    stack.pop()
                    destroyed = True
                    break
                else:
                    stack.pop()

            if destroyed == False:
                stack.append(ast)

        return stack
        