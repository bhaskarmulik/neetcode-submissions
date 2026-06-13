class Solution:

    def arr_hash(self, s):
        h = [0] * 52

        for ch in s:
            if 'A' <= ch <= 'Z':
                h[ord(ch) - ord('A')] += 1
            else:  # a-z
                h[26 + ord(ch) - ord('a')] += 1

        return h

    def minWindow(self, s: str, t: str) -> str:

        #Converting s into hash string for easier check
        main_hash = self.arr_hash(t)


        #Indices
        l =r =0
        maxl,maxr = 0,0
        max_seen = 1001

        while r < len(s):

            while all(self.arr_hash([x for x in s[l:r+1] if x in t])[i] >= main_hash[i] for i in range(52)):          
                window_len = r-l+1
                if window_len < max_seen:
                    max_seen = r-l+1
                    maxl = l
                    maxr = r
                l +=1

            r+=1
        
        if max_seen == 1001:
            return ""
        return s[maxl:maxr+1]