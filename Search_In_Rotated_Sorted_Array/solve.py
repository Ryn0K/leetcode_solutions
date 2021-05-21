from typing import List
class Solution:
  def search(self,nums:List[int],target:int) -> int:
    for i in range(len(nums)):
      if nums[i] == target:
        return i
    return -1
if __name__ == "__main__":
  s = Solution()
  print(s.search([4,5,6,7,0,1,2],0))
