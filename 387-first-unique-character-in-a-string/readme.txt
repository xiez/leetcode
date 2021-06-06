Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

 

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.

----------------------------------------

Solution 1:

first pass, use hashmap(letter -> count) to record the letter occurences,

seconds pass, enumerate the string to find first unique letter

Time: O(n)
Space: O(n)


