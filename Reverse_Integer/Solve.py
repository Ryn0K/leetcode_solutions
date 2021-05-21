class Solution:
    def reverse(self,x:int)-> int:
        x=str(x)
        if x[0] == "-": # negative
            a= int("-"+x[::-1][:-1])
            if a>=-2147483648 and a<=2147483648:
                return a
            else:
                return 0
        else:
            a = int(x[::-1])
            if a>=-2147483648 and a<=2147483648:
                return a
            else:
                return 0      
if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-120))