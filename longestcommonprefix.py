def longestCommonPrefix(strs):
        if not strs:
            return ""
        short = min(strs, key=len)
        for i, c in enumerate(short):
            for string in strs:
                if c != string[i]:
                    return short[:i]
        #return short for the case [""]
        return short

strs = ["acvsdf","acdfaefv","agwrtgbv"]

print(longestCommonPrefix(strs))