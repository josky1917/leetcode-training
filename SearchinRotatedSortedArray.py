class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        num = len(nums)
        left = 0
        right = num - 1
        if target < nums[left] and target > nums[right]:
            return -1
        while(left<right):
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if nums[left]<=nums[mid]:
                if target>=nums[left] and target<nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        if nums[left] == target:
            return left
        else:
            return -1