def myAtoi(str):
        s = str.strip()
        if not s:
            return 0
        start = 0
        sign = 1
        
        value = 0
        if s[0] == '+':
            start = 1
        elif s[0] == '-':
            start = 1
            sign = -1
        elif not s[0].isdigit():
            return 0
        l = len(s)
        while start < l and s[start].isdigit():
            value = value * 10 + int(s[start])
            start += 1
        
        value *= sign
        maxvalue = 2**31-1
        minvalue = -2**31
        
        if value >maxvalue:
            return maxvalue
        elif value < minvalue:
            return minvalue
        else:
            return value

print(myAtoi("   -34sdf"))