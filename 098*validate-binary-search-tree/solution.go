/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import (
    "math"
    "fmt"
)


func auxIsValidBST(root *TreeNode, prev *int) bool {
    if root == nil {
        return true
    }
    
    if !auxIsValidBST(root.Left, prev) {
        return false
    } 
     
    if root.Val <= *prev {
        return false
    } else{
       *prev = root.Val     
    }

    if !auxIsValidBST(root.Right, prev) {
        return false
    }
    
    return true  
}

func isValidBST(root *TreeNode) bool {
    var prev int = int(math.Inf(-1))
    return auxIsValidBST(root, &prev)
    
}
