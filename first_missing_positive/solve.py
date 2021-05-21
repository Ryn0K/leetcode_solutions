from typing import List
class Solution:
  def firstMissingPositive(self,nums:List[int]) -> int:
    nums = sorted(nums)
    if len(nums) ==1 or  len(nums) ==0 :
      return 2 if 1 in nums else 1
    m = max(nums)
    if m >0:
      nnums = [i for i in range(1,m +2)]
      for nnum in nnums:
        if nnum in nums:
          continue
        else:
          return nnum
    return 1
if __name__ == "__main__":
  s = Solution()
  print(s.firstMissingPositive([1,2,0]))
  print(s.firstMissingPositive([3,4,-1,1]))
  print(s.firstMissingPositive([7,8,9,11,12]))
  print(s.firstMissingPositive([-1,-2,-4,-3,0]))
  print(s.firstMissingPositive([1]))
  print(s.firstMissingPositive([]))
  

