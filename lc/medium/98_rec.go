package medium

//func isValidBST(root *TreeNode) bool {
//	return isValidBSTRec(root, math.MinInt, math.MaxInt)
//}
//
//func isValidBSTRec(root *TreeNode, l, r int) bool {
//	if root == nil {
//		return true
//	}
//	if root.Val <= l || root.Val >= r {
//		return false
//	}
//	return isValidBSTRec(root.Left, l, root.Val) && isValidBSTRec(root.Right, root.Val, r)
//}
