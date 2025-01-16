class Solution:
    def isPalindrome(self, x: int) -> bool:
        ## Negative numbers are never palidrome's
        if x < 0: 
            return False
        ## Single digit numbers are always palidrome's
        elif x < 10:
            return True

        s = str(x)
        n = len(s)
        odd = False
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(n / 2 - 0.5)

        for i in range(n):
            if s[i] != s[-(i + 1)]:
                return False

        return True   
