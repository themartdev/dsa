package graph

type ListNode[T any] struct {
	Val  T
	Prev *ListNode[T]
	Next *ListNode[T]
}

type DoublyLinkedList[T any] struct {
	head *ListNode[T]
	tail *ListNode[T]
}

func NewDoublyLinkedList[T any]() DoublyLinkedList[T] {
	return DoublyLinkedList[T]{}
}

func (list *DoublyLinkedList[T]) Push(value T) {
	newNode := &ListNode[T]{
		Val:  value,
		Prev: nil,
		Next: nil,
	}

	if list.head == nil {
		list.head = newNode
		list.tail = newNode
	} else {
		newNode.Prev = list.tail
		list.tail.Next = newNode
		list.tail = newNode
	}
}

// Pop returns a tuple of the last element of the list and a boolean indicating
// if this element exists
func (list *DoublyLinkedList[T]) Pop() (T, bool) {
	list.invariants()
	var val T
	if list.tail == nil {
		return val, false
	}
	val = list.tail.Val
	list.tail = list.tail.Prev
	if list.tail == nil {
		list.head = nil
	}
	list.invariants()
	return val, true
}

func (list *DoublyLinkedList[T]) PushFront(value T) {
	list.invariants()
	newNode := &ListNode[T]{
		Val:  value,
		Prev: nil,
		Next: nil,
	}

	if list.head == nil {
		list.head = newNode
		list.tail = newNode
	} else {
		newNode.Next = list.head
		list.head.Prev = newNode
		list.head = newNode
	}
	list.invariants()
}

func (list *DoublyLinkedList[T]) PopFront() (T, bool) {
	list.invariants()
	var val T
	if list.head == nil {
		return val, false
	}
	val = list.head.Val
	list.head = list.head.Next
	if list.head == nil {
		list.tail = nil
	}
	list.invariants()
	return val, true
}

func (list *DoublyLinkedList[T]) Empty() bool {
	return list.head != nil
}

func (list *DoublyLinkedList[T]) Front() *ListNode[T] {
	return list.head
}

func (list *DoublyLinkedList[T]) Back() *ListNode[T] {
	return list.head
}

func (list *DoublyLinkedList[T]) invariants() {
	if (list.head == nil && list.tail != nil) ||
		(list.head != nil && list.tail == nil) {
		panic("Head and tail can only be nil at the same time")
	}
}
