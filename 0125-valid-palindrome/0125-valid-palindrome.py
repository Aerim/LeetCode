class Solution:
    def isPalindrome(self, s: str) -> bool:
        
#         s1 = ""
#         for i in range(len(s)):
#             if s[i].isalnum() :
#                 s1 += s[i].lower()
                
#         if s1 == s1[::-1]:
#             return True
#         else:
#             return False

        s1 = ""
        for i in range(len(s)):
            if s[i].isalnum() :
                s1 += s[i].lower()
                
        left = 0
        right = len(s1) - 1
        
        while left < right:
            if s1[left] != s1[right]:
                return False
            
            else:
                left += 1
                right -= 1
        
        return True