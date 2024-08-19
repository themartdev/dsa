package medium

func levelOrder(root *TreeNode) [][]int {
	order := make([][]int, 0)

	currentLevel := make([]*TreeNode, 0)
	nextLevel := make([]*TreeNode, 0)
	if root != nil {
		nextLevel = append(nextLevel, root)
	}

	depth := 0
	for len(nextLevel) != 0 {
		currentLevel = nextLevel
		nextLevel = make([]*TreeNode, 0)
		order = append(order, make([]int, 0, len(currentLevel)))

		for _, node := range currentLevel {
			order[depth] = append(order[depth], node.Val)
			if node.Left != nil {
				nextLevel = append(nextLevel, node.Left)
			}
			if node.Right != nil {
				nextLevel = append(nextLevel, node.Right)
			}
		}

		depth += 1
	}
	return order
}
