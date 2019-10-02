class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        res = [0, 0]
        num = len(nums)
        left = 0
        right = num-1
        while(left < right-1):
            mid = left+(right-left)//2
            if nums[mid]<target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            res[0] = left
        elif nums[right] == target:
            res[0] = right
        else:
            res[0] = -1
        left = 0
        right = num-1
        while(left < right-1):
            mid = left+(right-left)//2
            if nums[mid]>target:
                right = mid
            else:
                left = mid
        if nums[right] == target:
            res[1] = right
        elif nums[left] == target:
            res[1] = left
        else:
            res[1] = -1
        return res