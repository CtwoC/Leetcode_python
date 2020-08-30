# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #a compare function
        ans = collections.defaultdict(list)
        #sorted() sort chars in order
        #use tuple(sorted(s)) to get single chars of these strings as our dic key
        #use string as our value of these keys
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

#Use the function defaultdict to solve problems using dictionary
#example:
#%%
import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
# d.items()
# d.values()

# %%
