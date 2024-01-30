class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max=pow(2, 31)
        min = -pow(2, 31)
        max = max -1
        ans=0
        neg = False
        if(x<0):
            neg = True
            x= -x
        while(x>0):
            ans= ans + (x%10 )
            ans=ans * 10
            x= x//10
             
        if(neg):   
            ans = -ans     
        ans = ans//10
        if ans > max or ans < min:
            return 0
        else:
            return ans

# Instantiate the Solution class
solution_instance = Solution()


print(solution_instance.reverse(123))
