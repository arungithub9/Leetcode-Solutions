# Leetcode Valid Palindrome Python Solution
# Done By : arunachalam.codes
# https://leetcode.com/problems/valid-palindrome/

#  Explanation : Coming Soon!
#  O(n) time solution without extra space 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #empty string condition
        if s == "":
            return True
        
        #normal strings        
        s = s.lower()
        size = len(s)
        ptr1, ptr2 = 0, size -1
        isPalin = True
        while ptr1 < ptr2:
            while s[ptr1].isalnum() == False:
                ptr1 +=1
                if ptr1 == size -1:
                    return isPalin
            while s[ptr2].isalnum() == False:
                ptr2 -=1
                if ptr2 == 0:
                    return isPalin
            if s[ptr1] != s[ptr2]:
                isPalin = False
                break
            else:
                ptr1 +=1
                ptr2 -=1
        
        return isPalin
                