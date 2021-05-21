from typing import List
class Solution:
  def searchRange(self,nums:List[int],target:int) -> List[int]:
    if len(nums) == 0:
      return list((-1,-1))
    left = 0
    right = len(nums) - 1
    while (left < right):
      mid = (left + right)//2
      if nums[mid] < target:
        left = mid + 1
      else:
        right = mid
    if nums[left] != target:
      return list((-1,-1))
    else:
      left_ans = left
    left = 0
    right = len(nums) - 1
    while (left < right):
      mid = (left + right)//2
      if target < nums[mid]:
        right = mid
      else:
        left = mid + 1
    if nums[left] != target:
      right_ans = left - 1
    else:
      right_ans=left
    return list((left_ans,right_ans))
if __name__ == "__main__":
  s = Solution()
  print(s.searchRange([5,7,7,8,8,10],8))

