class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0,len(height)-1
        maximumarea,maximumwidth=0,len(height)-1
        for currentWidth in range(maximumwidth,0,-1):
            if height[l]<height[r]:
                maximumarea=max(maximumarea,height[l]*currentWidth)
                l+=1
            elif height[r]<=height[l]:
                maximumarea=max(maximumarea,height[r]*currentWidth)
                r-=1
        return maximumarea     
        