# Leetcode String to Integer (ATOI) Solution
# Done By : arunachalam.codes
# https://leetcode.com/problems/string-to-integer-atoi/

#Explanation : Coming Soon!


class Solution:
    def myAtoi(self, str: str) -> int:  #0 -> 48, 9 -> 57 ascii val
        int_min = -2147483648
        int_max =  2147483647
        ans = 0
        nonLetterSign = False
        positive = True
        for char in str:
            if ord(char) >=48 and ord(char) <= 57:
                ans = ans * 10
                ans = ans + ord(char) - 48
                nonLetterSign = True
            elif char == '-':
                if nonLetterSign == False:
                    positive = False
                    nonLetterSign = True
                else:
                    break
            elif char == '+':
                if nonLetterSign == False:
                    nonLetterSign = True
                else:
                    break
            elif char != ' ':
                break
            else:
                if nonLetterSign == True:
                    break
        
        if positive == True:
            ans = min(int_max,ans)
        else:
            ans = -ans
            ans = max(int_min,ans)
        
        return ans
        
        
                
                