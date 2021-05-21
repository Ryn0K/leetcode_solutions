from typing import List
class Solution:
  areas = list()
  def maxArea(self,height:List[int]) -> int:
    for i in range(len(height)):
      for j in range(len(height)):
        if height[i] < height[j]:
          self.areas.append(int(height[i]*abs(i-j)))
        elif height[i] > height[j]:
          self.areas.append(int(height[j]*abs(i-j)))
        else:
          self.areas.append(int(height[j]*abs(i-j)))
    return max(self.areas)
if __name__ == "__main__":
  #height=[1,8,6,2,5,4,8,3,7]
  height=[4,3,2,1,4]
  s = Solution()
  print(s.maxArea(height))

