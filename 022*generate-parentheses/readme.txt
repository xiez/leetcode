Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8

----------------------------------------

1. bruteforce

when n = 1, result is "()",

start from 2 to n, at each iteration, generate parenthesis based on current result


2. https://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/
