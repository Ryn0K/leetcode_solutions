from typing import List
class Solution:
  def searchInsert(self,nums:List[int],target:int) -> int: 
    l = 0
    r = len(nums)  - 1
    while(l<r):
      mid = (l+r)//2
      if nums[mid]<target:
        l = mid + 1
      else:
        r = mid
    if nums[l] == target:
      return l 
    elif nums[l] > target:
      return l
    else:
      return l + 1
if __name__ == "__main__":
  s = Solution()
  print(s.searchInsert([0,2,3,5,6],1))
