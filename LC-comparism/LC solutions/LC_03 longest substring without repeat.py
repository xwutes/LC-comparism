# LC_03 longest substring without repeating characters

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] > 0:                      # the second time an element comes out, original count of 
                                                        # one time still exist will triger counter var
                counter += 1                            # counter will record numbers as pointer moves alone the list
            lookup[s[end]] += 1                         
            end += 1                                    # this one is the running pointer
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1                              
            max_len = max(max_len, end - start)         # sliding window will eventually have this sentense 
        return max_len                                  # elements inside this expression will have the beginning and ending of this 