from typing import List
class Solution:
  def twoSum(self,nums : List[int],target : int) -> List[int]:
    nums = sorted(nums)
    left = 0
    right = len(nums)-1
    result = []
    while ( left < right ):
      s = nums[left] + nums[right]
      if s < target:
        left += 1
      elif s > target:
        right -= 1
      else:
        result.append(left)
        result.append(right)
        return result
if __name__ == "__main__":
  nums = [2,7,11,15]
  target = 9
  s = Solution()
  print(s.twoSum(nums,target))
