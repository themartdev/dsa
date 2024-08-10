package collisions

type ListNode struct {
	Val  int
	Next *ListNode
}

func sortList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	length := 0
	curr := head
	for curr != nil {
		length += 1
		curr = curr.Next
	}
	return sort(head, length)
}

func sort(head *ListNode, n int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	left, right, mid := split(head, n)
	l := mid
	r := n - l
	left = sort(left, l)
	right = sort(right, r)
	return merge(left, right)
}

func split(head *ListNode, n int) (*ListNode, *ListNode, int) {
	mid := n / 2
	current := head
	for i := 1; i < mid; i++ {
		current = head.Next
	}
	right := current.Next
	current.Next = nil
	return head, right, mid
}

func merge(left, right *ListNode) *ListNode {
	dummy := &ListNode{}
	curr := dummy

	for left != nil && right != nil {
		if left.Val < right.Val {
			curr.Next = left
			left = left.Next
		} else {
			curr.Next = right
			right = right.Next
		}
		curr = curr.Next
	}

	if left != nil {
		curr.Next = left
	}
	if right != nil {
		curr.Next = right
	}

	return dummy.Next
}
