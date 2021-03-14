Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

 
Follow up: The overall run time complexity should be O(log (m+n)).

----------------------------------------

# Naive solution

Time: O(max{m,n})
Space: O(max{m,n})

# Binary search

idea from https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46

Two arrays (A, B), A is the larger one

the final array that last element (or two) is the median, the length (N) of final array is (m+n) / 2 + 1

the final array contains at least one element from A, and at most all elements from A

## meet the median condition

array A: ... x x'
array B: ... y y'

if x >= y and x <= y' or y >= x and y <= x', then we can get the median of two arrays

## pseudo code:

for i=1 to N:
    A contributes i element(s), B contributes (N-i) elements
    if this meet the median condition, then we can get the median

we can improve the iteration using binary search to find the i,

low = 0
high = N
mid = (low + high) / 2

while True:
      A contributes mid element(s), B contributes (N-mid) elements
      if this meet the median condition, the we can get the median
      else:
        we should expand/shrink the range depends on median condition

        expand: low = mid+1
        shrink: high = mid-1
        calculate new mid element(s)








