def lengthOfLongestSubstring(s):
        NUM_CHARS=256
        len_s=len(s)
        #for the case of an empty string
        if len_s==0:
            return len_s

        max_len=1
        #starting index of the current non-repeating substring
        start_ind=0
        #initialize hash table of the index at which each character is visited
        #-1 means has not been visited
        visited=[-1]*NUM_CHARS
        
        #visit first character
        visited[ord(s[0])] = 0
        
        #loop thru rest of characters
        for curr_ind in range(1,len_s):
            #get the ascii number for current character
            curr_char = ord(s[curr_ind])
            #obtain when it was last visited
            last_visited=visited[curr_char]
            #if it has not been visited and the starting index is before its last visit, 
            #move starting index of current non-repeating substring to one index after 
            #the last visit
            if last_visited!=-1 and (start_ind < last_visited +1):
                start_ind=last_visited+1
            #get the length of the current non-repeating substring
            curr_len = curr_ind-start_ind+1
            #if the length is greater than the prevous greatest, update the greatest
            if max_len<curr_len:
                max_len=curr_len
            #mark the current char as visited at the current index
            visited[curr_char]=curr_ind
        return max_len

print(lengthOfLongestSubstring("abcdbaea"))