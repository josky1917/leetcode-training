def longestPalindrome(s):
        if not s : return s
        
        res = ""
        for i in range(0, len(s)):            
            n = 0
            m = 0
            while s[i-n:i+n+1] == s[i-n:i+n+1][::-1] and i-n>= 0 and i+n <= len(s)-1:
                if len(s[i-n:i+n+1])>len(res):
                    res = s[i-n:i+n+1]
                n += 1
            while s[i-m:i+m+2] == s[i-m:i+m+2][::-1] and i-m>=0 and i+m+1 <=len(s)-1:
                if len(s[i-m:i+m+2])>len(res):
                    res = s[i-m:i+m+2]
                m += 1
                
        return res

s = "acdfgegfdekid"
print(longestPalindrome(s))