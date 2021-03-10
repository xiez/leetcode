Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

 

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?

----------------------------------------

## naive approach

traverse list to get the length, add first half to stack, compare with second half

Time: O(n)
Space: O(n)

## build first half to point back

traverse list to get the length,
use three pointers(prev, curr, next) to build first half nodes to point backwards, and keep compare from middle point

Time: O(n)
Space: O(1)




