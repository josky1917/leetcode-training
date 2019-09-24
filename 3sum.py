def threeSum(nums):
        nums.sort()
        num = len(nums)
        res = []
        for i in range(num-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = num -1
            if nums[i]+nums[i+1]+nums[i+2]>0:
                return res
            while(l < r):
                s = nums[i]+nums[l]+nums[r]
                if s == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[l] == nums[l+1]):
                        l += 1
                    while(l<r and nums[r] == nums[r-1]):
                        r -= 1
                    l += 1
                    r -= 1
                elif s <0:
                    l += 1
                elif s >0:
                    r -= 1
        return res

print(threeSum([1,3,4,34,-4,-6,-8,-14,32,4,5,6,-8]))