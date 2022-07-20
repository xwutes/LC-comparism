# LC_159 Longest Substring with At Most Two Distinct Characters
import collections

class Solution:
    def lenthOfLongestSubstringTwoDistinct(self, s:str)-> int:
        max_len, start, end, counter = 0,0,0,0
        char_dict = collections.defaultdict(int)
        while end < len(s):
            if char_dict[s[end]] == 0:              # == 0 means first occurance
                counter += 1                        # count occurance time
            char_dict[s[end]] += 1
            end += 1                                # end 仅限于在n这个数字范围内进行累加
            while counter > 2:                      # two distinct means counter should less than 2
                char_dict[s[start]] -= 1            # > 2的背后是在前面的指针start扫到了后面重复的元素,所以计数要加一, 在这里减回来.
                if char_dict[s[start]] == 0:
                    counter -= 1
                start += 1

            max_len = max(max_len, end - start)

        return max_len


def lenthOfLongestSubstringTwoDistinct(self, s:str)-> int:
    start, end, max_len, counter = 0,0,0,0
    char_dict = collections.defaultdict(int)
    n = len(s)
    while end < n:
        if char_dict[s[end]] == 0:
            counter += 1
        char_dict[s[end]] += 1
        end += 1
        while counter > 2:
            char_dict[s[start]] -= 1                    # counter 在第一段时候已经记录的第一次出现
            if char_dict[s[start]] == 0:                # 这边再次出现一定是相同的字母
                counter -= 1
            start += 1                                  # start这边累加可以将数值变的更大

        max_len = max(max_len, end-start)
    
        return max_len