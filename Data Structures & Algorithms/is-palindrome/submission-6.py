class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        word = "".join(x.lower() for x in s if x.isalnum())
        left = 0
        right = len(word)-1
        while left < right:
            if word[left] != word[right]:
                return False
            left = left+1
            right = right -1 
            
        return True 



        
