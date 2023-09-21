class Solution(object):
    def isPalindrome(self, x):
       
        if x < 0:
            return False
        
        temp = x
        rev =  0 
        
        # 직접 뒤집기
        while temp != 0:
            res = temp % 10
            rev = rev * 10 + res
            
            temp = temp // 10
            
        return rev == x
            