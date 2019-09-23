def maxArea(height):
        maxarea = 0
        left = 0
        right = len(height)-1
        
        while(left != right):
            wid = right - left
            if height[left] > height[right]:
                area = wid*height[right]
                right = right - 1
            else:
                area = wid*height[left]
                left = left + 1
            if area > maxarea:
                maxarea = area
        
        return maxarea

print(maxArea([1,8,4,9]))