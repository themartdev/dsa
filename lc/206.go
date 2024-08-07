package main

func main() {

}

func reverseList(head *ListNode) *ListNode {
	oldHead := head
	var newHead *ListNode
	for oldHead != nil {
		buf := oldHead.Next
		oldHead.Next = newHead
		newHead = oldHead
		oldHead = buf
	}
	return newHead
}
