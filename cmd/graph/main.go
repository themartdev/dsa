package main

import "github.com/simon-martineau/dsa/internal/graph"

func main() {
	g := graph.NewEmpty[int](5)

	g.AddEdge(0, 1)
	g.AddEdge(0, 2)

	g.AddEdge(1, 4)
	g.AddEdge(1, 2)

	g.AddEdge(4, 3)
}
