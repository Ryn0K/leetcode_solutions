from typing import List

#define class
class Solution:
    #define method having type checking to accept List[int] and return List[List[int]]
    result = list()
    def threeSum(self,nums : List[int]) -> List[List[int]]:
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                for k in range(0,len(nums)):
                    if (nums[i]+nums[j]+nums[k] == 0) and (nums[i]!=nums[j]) and (nums[j]!=nums[i]) and (nums[k]!=nums[i]):
                        if list((nums[i],nums[j],nums[k])) not in self.result:
                            self.result.append(list((nums[i],nums[j],nums[k])))
        return self.result             
s=Solution().threeSum(nums=[-1,0,1,2,-1,-4])
print(s)