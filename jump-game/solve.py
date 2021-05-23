from typing import List
class Solution:
  def canJump(self,num:List[int]) -> bool:
    curr = 0
    end = len(num) - 1
    for i in range(len(num)):
      if i > curr:
        return False
      if curr < num[i] + i:
        curr = num[i] + i
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
