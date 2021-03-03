Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

 

Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

----------------------------------------

Similar to 026, two pointers(i, j) initialize to 0, 1

if L[i] overlaps with L[j], merge L[j] to L[i], delete L[j] util that L[i] and L[j] no longer overlap

continue iteration until j reach the end of list.

Note that first thing to do is to sort the invervals

Time: O(logN + N*N)

sort: O(logN)

every iteration delete element from array and move rest elements forward: O(n)

Space: O(1)

