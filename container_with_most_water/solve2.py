from typing import List
class Solution:
  def maxArea(self,a:List[int]) -> int:
    i = 0 # first element index
    j = len(a)-1 # last element index
    m = 0 # set max to zero
    while ( i < j ): # always start the loop until i < j
      m = max(m,min(a[i],a[j])*(j-i))# example : max(0,min(1,7)*(8-0)) => max(0,8) => 8 = m 
      if ( a[i] < a[j] ): # 1 < 7 no need for 1 to compare with another one
        i += 1 # i = 8
      else:
        j -= 1
    print(m)
if __name__ == "__main__":
  height = [1,8,6,2,5,4,8,3,7]
  s = Solution()
  s.maxArea(height)
