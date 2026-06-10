#valid palindrome
'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
A palindrome string is a string that is read the same from the start as well as from the end. This means the character at the start should match the character at the end at the same index. We can use the two pointer algorithm to do this efficiently.
'''

'''
For Valid Palindrome, the optimal approach is to use two pointers:

One pointer starts at the beginning (left).
One pointer starts at the end (right).
Skip any non-alphanumeric characters.
Compare characters in lowercase form.
If they don't match, return False.
If all pairs match, return True.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# Example usage
solution = Solution()

s = "Was it a car or a cat I saw?"
print(solution.isPalindrome(s))