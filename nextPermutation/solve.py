from typing import List

class Solution:
    def nextPermutation(self,nums:List[int]) -> None:
      #find the longest increasing suffix(pivot)
      right = len(nums)-1
      if right < 0:
        return None
      while(right>0 and nums[right-1] >= nums[right]):
        right-=1
      if right == 0:
        nums[:]=nums[::-1]
        print(nums)
        return 
      left = right-1
      right = len(nums) - 1
      while(nums[left]>= nums[right]):
        right-=1
      nums[left],nums[right] = nums[right],nums[left]
      nums[left+1:]=nums[left+1:][::-1]
if __name__ == "__main__":
    s = Solution()
    s.nextPermutation([3,2,1])
