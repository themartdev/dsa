package main

import (
	"fmt"
	"strings"
)

func main() {
	res := generateParenthesis(1)
	fmt.Printf("%v", res)
}

func generateParenthesis(n int) []string {
	stack := make([]string, 0)
	res := make([]string, 0)

	var backtrack func(nOpen, nClosed int)
	backtrack = func(nOpen, nClosed int) {
		if nOpen == n && nClosed == n {
			res = append(res, strings.Join(stack, ""))
		}
		if nOpen > nClosed {
			stack = append(stack, ")")
			backtrack(nOpen, nClosed+1)
			stack = stack[:len(stack)-1]
		}
		if nOpen < n {
			stack = append(stack, "(")
			backtrack(nOpen+1, nClosed)
			stack = stack[:len(stack)-1]
		}
	}

	backtrack(0, 0)
	return res
}
