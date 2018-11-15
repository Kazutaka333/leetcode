class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = {"(":0,"{":1,"[":2}
        
        right = [")","}","]"] 
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if len(stack) > 0 and c == right[left[stack[-1]]]:
                    stack = stack[:-1]
                else:
                    return False
        return len(stack) == 0

s = Solution()
print(s.isValid("()"))
print(s.isValid(")"))
