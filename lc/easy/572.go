package easy

/*
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
*/

func isSubtree(root, subRoot *TreeNode) bool {
	if root == nil && subRoot == nil {
		return true
	} else if root == nil || subRoot == nil {
		return false
	}

	if root.Val == subRoot.Val {
		if treeEquals(root, subRoot) {
			return true
		}
	}
	return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}

func treeEquals(a, b *TreeNode) bool {
	if a == nil && b == nil {
		return true
	} else if a == nil || b == nil {
		return false
	}
	return a.Val == b.Val && treeEquals(a.Left, b.Left) && treeEquals(a.Right, b.Right)
}
