from typing import List

#define the Solution class
class Solution:
    #define twoSum() method in which two methods of having these must type and return list of int.
    def twoSum(self,nums:List[int],target : int) -> List[int]: 
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (nums[i]+nums[j] == target) and (i < j):
                    return list((i,j))
print(Solution().twoSum([2,4,5,6,9],9))
