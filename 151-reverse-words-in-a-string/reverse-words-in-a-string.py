class Solution(object):
    def reverseWords(self, s):
        l=len(s)
        s=s.split()
        
        s=s[::-1]
        return " ".join(s)
        