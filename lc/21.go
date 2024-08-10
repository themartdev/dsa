package main

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	head := &ListNode{}
	tail := head

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			tail.Next = list1
			tail = list1
			list1 = list1.Next
			tail.Next = nil
		} else {
			tail.Next = list2
			tail = list2
			list2 = list2.Next
			tail.Next = nil
		}
	}

	for list1 != nil {
		tail.Next = list1
		tail = list1
		list1 = list1.Next
		tail.Next = nil
	}

	for list2 != nil {
		tail.Next = list2
		tail = list2
		list2 = list2.Next
		tail.Next = nil
	}

	return head.Next
}
