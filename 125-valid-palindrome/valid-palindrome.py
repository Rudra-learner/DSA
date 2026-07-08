class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        q=""
        for ch in s:
            if ch.isalnum()==True:
                q+=ch
            else:
                continue
        
        if(q==q[::-1]):
            return True
        else:
            return False


       
        