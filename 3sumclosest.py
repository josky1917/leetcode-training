def threeSumClosest(nums, target):
        nums.sort()
        num = len(nums)
        res = nums[0]+nums[1]+nums[2]
        for i in range(num-2):
            l = i + 1
            r = num -1
            while(l < r):
                s = nums[i]+nums[l]+nums[r]
                if s == target:
                    return target
                if abs(s-target) < abs(res-target):
                        res = s
                if s>target:
                    r -= 1
                if s<target:
                    l += 1
        return res

print(threeSumClosest([1,3,4,5,6,23,46,3,-1,-4,-6],12))