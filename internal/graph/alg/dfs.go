package alg

import "github.com/simon-martineau/dsa/internal/graph"

func DFS(g *graph.AdjGraph, start int, visit func(node int)) {
	stack := make([]int, 0)
	stack = append(stack, start)
	visited := make([]bool, g.Size())
	visit(start)

	for len(stack) > 0 {
		curr := stack[len(stack)-1]
		neighbors := g.Neighbors(curr)
		for neighbor, ok := neighbors.PopFront(); ok; {
			if !visited[neighbor] {
				stack = append(stack, neighbor)
				visit(neighbor)
			}
		}
	}
}
