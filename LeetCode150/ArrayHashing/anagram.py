# Valid Anagram
"""
Given two strings s and t, return true if the two strings are anagrams of each other, 
otherwise return false.

An anagram is a string that contains the exact same characters as another string,
 but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
Recommended Time & Space Complexity
You should aim for a solution with O(n + m) time and O(1) space,
 where n is the length of the string s and m is the length of the string t.

"""
# My approach
"""
I would create an empty hash table, store s string in it
and run a compare loop to compare t with s and if all has a match we 
will return output to true
"""
##optimal approach
"""
we will maintain frequency of each character. we can do this by having two
separate hash tables for two strings. then,we can check whether the frequency of each 
character in string s is equal to that in string t and vice versa
"""

def Anagram(s,t):
    #check length of both string s& t, return true if matches else false
    if len(s) != len(t):
        return False
    #hash the 26 small letters a-z
    count = [0] * 26

    for i in range(len(s)):
        """
        we run a loop in string s so that we can count the order of s and 
        subtract it from above hash list and increase by 1 for string s
        and same thing for string t count the order of char in string t
        subtract it from order of hash table and decrease by 1.
        this way if count return 0, its true if not false.
        """
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord("a")] -=1
    
    for c in count:
        if c != 0:
            return False
    return True

print(Anagram("racecar", "carrace"))