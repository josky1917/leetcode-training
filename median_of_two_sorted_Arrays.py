def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if m > n:
        m, n, nums1, nums2 = n, m, nums2, nums1
    if n == 0:
        raise ValueError
            
    imin, imax, half_len = 0, m, (m+n+1)/2
    while imin <= imax:
        i = int((imin + imax)/2)
        j = int(half_len - i)
        if i<m and nums2[j-1]>nums1[i]:
            imin = i + 1
        elif i>0 and nums2[j]<nums1[i-1]:
            imax = i - 1
        else:
            if i == 0:
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])
            
            if (n+m) % 2 == 1:
                return max_of_left
            
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i],nums2[j])
                    
            return (max_of_left + min_of_right) / 2.0

num1 = {0: 2,1: 4,2: 6,3: 8}
num2 = {0: 3,1: 5,2: 7}
print (findMedianSortedArrays(num1, num2))