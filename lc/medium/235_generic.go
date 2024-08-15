package medium

import "fmt"

// I didn't see it was a BST, so this solution is for any type of tree ... :')

func lowestCommonAncestorGeneric(root, p, q *TreeNode) *TreeNode {
	pStack, _ := findNode(root, p, []*TreeNode{})
	qStack, _ := findNode(root, q, []*TreeNode{})

	if pStack[0] != qStack[0] {
		fmt.Printf("pStack: %v\nqStack: %v\n", pStack, qStack)
		panic("should not happen")
	}

	lowest := pStack[0]
	for i := 1; i < len(pStack) && i < len(qStack); i++ {
		if pStack[i] == qStack[i] {
			lowest = pStack[i]
		} else {
			break
		}
	}
	return lowest
}

func findNode(curr, p *TreeNode, stack []*TreeNode) ([]*TreeNode, bool) {
	if curr == nil {
		return stack, false
	}
	stack = append(stack, curr)
	if curr == p {
		return stack, true
	}
	leftStack, leftFound := findNode(curr.Left, p, stack)
	if leftFound {
		return leftStack, true
	}
	return findNode(curr.Right, p, stack)
}
