class Solution(object):
    def sumAndMultiply(self, n):
        x=0
        while(n!=0):
            d=n%10
            if(d!=0):
                x=x*10+d
                n//=10
            else:
                n//=10
        rev=0
        while(x!=0):
            rev=rev*10+x%10
            x//=10
        y=rev
        sum=0
        while(y!=0):
            z=y%10
            sum=sum+z
            y//=10
        
        q=rev*sum
        return q
            
      
        
        
        
        
        
        
        



        
        