def fourSum(nums, target):
        nums.sort()
        num = len(nums)
        res = list()
        if num<4:
            return res
        for i in range(num-3):
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            for j in range(i+1 , num - 2):
                if nums[i]+nums[j]+nums[j+1]+nums[j+2]>target:
                    break
                l = j+1
                r = num -1
                while (l<r):
                    sum = nums[i]+nums[j]+nums[l]+nums[r]
                    if sum == target:
                        if [nums[i],nums[j],nums[l],nums[r]] not in res:
                            res.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        r -= 1
                    elif sum > target:
                        r -= 1
                    else:
                        l += 1
        return res

print(fourSum([2,3,4,5,-1,-5,-6,8],3))