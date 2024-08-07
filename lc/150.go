package main

import (
	"strconv"
)

func main() {

}

func evalRPN(tokens []string) int {
	stack := make([]int, 0)
	for _, token := range tokens {
		isNum, num := isNumber(token)
		if !isNum {
			a, b := stack[len(stack)-2], stack[len(stack)-1]
			stack = stack[:len(stack)-2]
			switch token {
			case "+":
				stack = append(stack, a+b)
				break
			case "-":
				stack = append(stack, a-b)
				break
			case "*":
				stack = append(stack, a*b)
				break
			case "/":
				stack = append(stack, a/b)
				break
			}
		} else {
			stack = append(stack, num)
		}
	}
	if len(stack) != 1 {
		panic("Stack should have length of 1")
	}
	return stack[0]
}

func isNumber(token string) (bool, int) {
	// we assume all numbers are correctly formatted
	res, err := strconv.ParseInt(token, 10, 32)
	return err == nil, int(res)
}
