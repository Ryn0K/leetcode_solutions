from typing import List

class Solution:
    def threeSum(self,nums:List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)    
        if len(nums) < 3:
            return result # if nums has less than 3 elements
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                value = -1*nums[i]
                if s == value:
                    res=list((nums[i],nums[l],nums[r]))
                    if res not in result:
                        result.append(res)
                    l += 1
                    r -= 1
                elif s < value:
                    l += 1
                else:
                    r -= 1
        return result
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    print(s.threeSum(nums))