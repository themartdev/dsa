package graph

type AdjGraph struct {
	adj []DoublyLinkedList[int]
}

func NewEmpty(n int) *AdjGraph {
	g := &AdjGraph{
		adj: make([]DoublyLinkedList[int], n),
	}
	return g
}

func NewFromAdj[T any](list []DoublyLinkedList[int]) *AdjGraph {
	g := &AdjGraph{
		adj: list,
	}
	return g
}

func (g *AdjGraph) AddEdge(from int, to int) {
	g.adj[from].Push(to)
}

func (g *AdjGraph) AddVertex() {
	g.adj = append(g.adj, NewDoublyLinkedList[int]())
}

func (g *AdjGraph) Neighbors(node int) DoublyLinkedList[int] {
	return g.adj[node]
}

func (g *AdjGraph) Size() int {
	return len(g.adj)
}
