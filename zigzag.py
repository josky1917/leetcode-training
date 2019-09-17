def convert(s, numRows):
        if numRows == 1:
            return s
        k = numRows * 2 - 2
        res = ""
        num = len(s)
        nk = int(num / k)
        for i in range(numRows):
            for j in range(nk+1):
                if i == 0 or i == numRows-1:
                    if (j * k + i) < num:
                        res = res + s[j * k + i]
                else:
                    if (j * k + i) < num:
                        if (j * k + k - i) >= num:
                            res = res + s[j * k + i]
                        else:
                            res = res + s[j * k + i] + s[j * k + k - i]
        return res

print (convert("ADCVIWDFNSKDQWFDC", 3))