from typing import List
class Solution:
  def canJump(self,num:List[int]) -> bool:
    curr = 0
    end = len(num) - 1
    for i in range(len(num)):
      jump = num[i]+i
      if i > curr:
        return False
      if curr < jump:
        curr = jump 
      if curr >= end:
        return True
if __name__ == "__main__":
  s = Solution()
  print(s.canJump([2,3,1,1,4]))
  print(s.canJump([3,2,1,0,4]))
  print(s.canJump([0,3,4]))
  print(s.canJump([2,0,0]))
  print(s.canJump([1,2,3]))
  print(s.canJump([3,2,1]))
  print(s.canJump([2,5,0,0]))
