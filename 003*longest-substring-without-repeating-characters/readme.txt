Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

----------------------------------------

## naive approach

two pointers(i, j), a hashmap(dict), len_str to record the length of longest substring

init i, j = 0, 1

push s[j] to dict, move j to next, if s[j+1] in dict, compare current length with len_str, and  abort

continue iteration until i reach the end of string.


Time: O(n*n)

Space: O(n)
