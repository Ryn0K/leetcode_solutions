from typing import List
class Solution:
  def jump(self,nums:List[int]) -> int:
    end,curr,nex_,start,ans = len(nums) -1 ,-1 ,0,0,0
    while nex_ < end:
      if start > curr:
        ans+=1
        curr = nex_
      nex_ = max(nex_,nums[start] + start)
      start+=1
    return ans
if __name__ == "__main__":
  s = Solution()
  print(s.jump([3,2,2,4,5,6,7]))
