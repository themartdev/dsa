package medium

func copyRandomList(head *Node) *Node {
	if head == nil {
		return head
	}
	nodes := make([]*Node, 0)
	indices := make(map[*Node]int)
	cur := head
	for cur != nil {
		nodes = append(nodes, &Node{
			Val: cur.Val,
		})
		indices[cur] = len(nodes) - 1
		cur = cur.Next
	}

	cur, i := head, 0
	for cur != nil {
		if cur.Random != nil {
			idx, ok := indices[cur.Random]
			if !ok {
				panic("should not happen")
			}
			nodes[i].Random = nodes[idx]
		}
		if cur.Next != nil {
			nodes[i].Next = nodes[i+1]
		}
		cur = cur.Next
		i++
	}
	return nodes[0]
}
