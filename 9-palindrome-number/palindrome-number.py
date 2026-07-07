class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        str1=x[::-1]
        
        if(str1==x):
            return True
            
        else:
            return False
            
        
        