from typing import List
class Solution:
    def fourSum(self,nums : List[int],target : int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        if len(nums) < 4:
            return res
        for i in range(len(nums) - 3):
            for j in range(i+1,len(nums)-2):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if (s == target):
                        if list((nums[i],nums[j],nums[l],nums[r])) not in res:
                            res.append(list((nums[i],nums[j],nums[l],nums[r])))
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    elif s > target :
                        r -= 1
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([2,2,2,2,2],8))
    print(s.fourSum([1,0,-1,0,-2,2],0)) 