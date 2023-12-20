class Solution(object):
    def maxArea(self, height):
        leftIndex, rightIndex = 0, len(height) - 1
        maxWidth, maxArea = len(height) - 1, 0
        for currentWidth in range(maxWidth, 0, -1):
            if height[leftIndex] < height[rightIndex]:
                maxArea = max(maxArea, height[leftIndex] * currentWidth)
                leftIndex += 1
            else:
                maxArea = max(maxArea, height[rightIndex] * currentWidth)
                rightIndex -= 1
        return maxArea
