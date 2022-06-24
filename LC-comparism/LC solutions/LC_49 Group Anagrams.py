# LC_49 Group Anagrams
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = {}
    for i in strs:
        t = tuple(sorted(i))
        if t not in dic:
            dic[t] = [i]
        else:
            dic[t].append(i)
    return dic.values()

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)