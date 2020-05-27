# Leetcode Two Sum Python Solution
# Done By : arunachalam.codes
# https://leetcode.com/problems/two-sum/

#Explanation : Coming Soon!

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for x in range(0,len(nums)):
            if(target-nums[x] not in hashTable.keys()):
                hashTable[nums[x]]=x
            else:
                return[hashTable[target-nums[x]],x]
            