from typing import List
class Solution:
  def maxSubArray(self,nums:List[int]) -> int:
    start = nums[0]
    res = nums[0]
    for i in range(1,len(nums)):
      start = max(nums[i],nums[i] + start)
      res = max(start,res)
    return res
if __name__ == "__main__": 
  s = Solution()
  print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
  print(s.maxSubArray([1]))
  print(s.maxSubArray([5,4,-1,7,8]))
