package alg

import "github.com/simon-martineau/dsa/internal/graph"

func BFS(g *graph.AdjGraph, start int) (order []int) {
	if start < 0 || start > g.Size() {
		panic("BFS start index out of range for graph")
	}
	queue := graph.NewDoublyLinkedList[int]()
	queue.Push(start)
	visited := make([]bool, g.Size())
	visitedOrder := make([]int, 0, g.Size())
	visitedOrder = append(visitedOrder, start)
	visited[start] = true
	for curr, ok := queue.PopFront(); ok; {
		neighbors := g.Neighbors(curr)
		for neighbor, ok := neighbors.Pop(); ok; {
			visited[neighbor.Val] = true
			visitedOrder = append(visitedOrder, neighbor.Val)
			queue.Push(neighbor.Val)
		}
	}
	return visitedOrder
}
