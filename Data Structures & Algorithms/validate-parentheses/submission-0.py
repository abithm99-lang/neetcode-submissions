class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {")":"(","]":"[","}":"{"}

        for r in s:
            if r in hm:
                if stack and stack[-1] == hm[r]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(r)

        return True if not stack else False
        