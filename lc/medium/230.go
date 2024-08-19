package medium

func kthSmallest(root *TreeNode, k int) int {
	stack := make([]*TreeNode, 0)
	count := 0
	for root != nil || len(stack) > 0 {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		count++
		if count == k {
			return node.Val
		}
		root = node.Right
	}
	return -1
}
