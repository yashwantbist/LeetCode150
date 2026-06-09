"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

optimal approach
You should aim for a solution with O(m * n) time and O(m) space, 
where m is the number of strings and n is the length of the longest string.

We can simply use an array of size O(26), since the character set is a through z (26 continuous characters), 
to count the frequency of each character in a string. 
Then, we can use this array as the key in the hash map to group the strings.
"""
from collections import defaultdict

def groupAnagram(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        # Frequency array for 26 lowercase letters
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        # Convert list to tuple so it can be used as a dictionary key
        anagrams[tuple(freq)].append(s)

    # Return grouped anagrams as a list of lists
    return list(anagrams.values())


strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagram(strs))