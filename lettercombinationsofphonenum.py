def letterCombinations(digits):
        num = len(digits)
        dicts = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}
        if num == 0:
            return []
        else:
            res = list(dicts[digits[0]])
        for n in digits[1:]:
            temp = list()
            for element in dicts[n]:
                for string in res:
                    temp.append(string + element)
            res = temp
        return res

print(letterCombinations('25'))
                