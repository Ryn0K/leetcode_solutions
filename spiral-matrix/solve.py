from typing import List
class Solution:
  def spiralOrder(self,m:List[List[int]]) -> List[int]:
    self.res = list()
    self.spiral(len(m),len(m[0]),m)
    return self.res
  def spiral(self,row,col,m):
    top = 0
    bottom = row -1
    left = 0
    right = col - 1
    dr = 0
    while(top<=bottom and left<=right):
      if dr == 0:
        for i in range(left,right+1):
          self.res.append(m[top][i])
        top+=1
        dr = 1
      elif dr == 1:
        for j in range(top,bottom+1):
          self.res.append(m[j][right])
        right-=1
        dr = 2
      elif dr == 2:
        for k in range(right,left-1,-1):
          self.res.append(m[bottom][k])
        bottom-=1
        dr = 3
      elif dr ==3:
        for l in range(bottom,top-1,-1):
          self.res.append(m[l][left])
        left+=1
        dr = 0
if __name__ == "__main__":
  s = Solution()
  print(s.spiralOrder([[1]]))
  print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
  print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
