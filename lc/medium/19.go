package medium

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	tempHead := &ListNode{
		Next: head,
	}
	length := 0
	cur := tempHead.Next
	for cur != nil {
		length++
		cur = cur.Next
	}

	dropIdx := length - n
	idx := -1
	cur = tempHead
	for idx != dropIdx-1 {
		cur = cur.Next
		idx++
	}
	cur.Next = cur.Next.Next
	return tempHead.Next
}
