class Solution(object):
    def __init__(self):
        self.s = None
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        max_palind = ""
        for i in range(len(s)):
            # odd length
            p1 = self.maxPalidrom((i,i))   
            if len(p1) > len(max_palind):
                max_palind = p1

            # even length
            if i+1 < len(s) and s[i] == s[i+1]:
                p2 = self.maxPalidrom((i,i+1))   
                if len(p2) > len(max_palind):
                    max_palind = p2
        return max_palind

            
    def maxPalidrom(self, (left, right)):
        s = self.s
        while 0 <= left and right < len(self.s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[min(left+1, len(s)-1):max(right,0)]

