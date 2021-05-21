from typing import List
class Solution:
  def firstMissingPositive(self,nums:List[int]) -> int:
    if len(nums) == 1 or len(nums) == 0:
      return 2 if 1 in nums else 1
    # step 1 swap the numbers which are negative and greater than the length of array.
    if 1 not in nums:
      return 1
    for i in range(len(nums)):
      if (nums[i] <= 0 or nums[i] > len(nums)):
        nums[i] = 1
    # step 2 flip the state of number
    for i in range(len(nums)):
      ind = abs(nums[i]) - 1
      if nums[ind] > 0:
        nums[ind] = nums[ind] * (-1)
    #find first positive integer
    for i in range(len(nums)):
      if nums[i] > 0:
        return i + 1
    return len(nums) + 1
if __name__ == "__main__":
  s = Solution()
  print(s.firstMissingPositive([7,8,9,11,12]))
  print(s.firstMissingPositive([3,4,-1,1]))
  print(s.firstMissingPositive([7,8,9,11,12]))
