#Encode and DEcode
'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}
So Machine 1 does:

String encoded_string = encode(strs);
and Machine 2 does:

List<String> decoded_strs = decode(encoded_string);
decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: strs = ["Hello","World"]

Output: ["Hello","World"]
Explanation:

Solution solution = new Solution();
String encoded_string = solution.encode(strs);

// Machine 1 ---encoded_string---> Machine 2

List<String> decoded_strs = solution.decode(encoded_string);

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
solutions:
We can use an encoding approach where we start with a number representing the length of the string,
 followed by a separator character (let's use # for simplicity), 
and then the string itself. To decode, we read the number until we reach a #, 
then use that number to read the specified number of characters as the string.

Input lsit(strs{hello}) -> encode(length + # + strs) -> enoded string("5#hello")
-> decode(read N, skip#, read N chars) -> output list("hello")
'''


class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0

        while i < len(s):
            j = s.index("#", i)  # find the delimiter
            length = int(s[i:j])  # parse the length
            result.append(s[j + 1:j + 1 + length])  # read the string
            i = j + 1 + length  # move to next encoded string

        return result


# Driver code
solution = Solution()

strs = ["My name is Yashwant Bist"]

encoded = solution.encode(strs)
print("The encoded message is:", encoded)

decoded = solution.decode(encoded)
print("The decoded message is:", decoded)