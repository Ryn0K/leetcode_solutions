from typing import List
class Solution:
  def rotate(self,matrix:List[List[int]]) -> None:
    for i in range(len(matrix)):
      for j in range(i,len(matrix[i])):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for row in matrix:
      row.reverse()
if __name__ == "__main__":
  s = Solution()
  s.rotate([[1,2,3],[4,5,6],[7,8,9]])
  s.rotate([[1,2],[3,4]])
  s.rotate([[1]])
  s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
