from typing import List
class Solution:
  def trap(self,height:List[int]) -> int:
    ans=0
    if len(height) < 3:
      return 0
    left,right = 0,len(height) - 1
    left_max ,right_max= height[left],height[right]
    while (left < right):
      left_max = max(left_max,height[left])
      right_max = max(right_max,height[right])
      if left_max < right_max:
        ans+= left_max - height[left]
        left += 1
      else:
        ans+= right_max - height[right]
        right -= 1
    return ans
if __name__ == "__main__":
  s = Solution()
  print(s.trap([4,2,0,3,2,5]))
