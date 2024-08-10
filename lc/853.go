package main

import "fmt"

func carFleet(target int, position, speed []int) int {
	n := len(position)
	// assuming sorted position
	position, speed = sortByPosition(position, speed)
	fmt.Printf("position: %v, speed: %v\n", position, speed)

	stack := []float64{tminus(position[n-1], speed[n-1], target)}
	for i := n - 2; i >= 0; i-- {
		fmt.Printf("i=%d, stack: %v\n", i, stack)
		val := tminus(position[i], speed[i], target)
		fmt.Printf("val=%v\n", val)
		if val > stack[len(stack)-1] {
			stack = append(stack, val)
		}
	}
	return len(stack)
}

func tminus(position, speed, target int) float64 {
	return float64(target-position) / float64(speed)
}

func sortByPosition(position, speed []int) ([]int, []int) {
	if len(position) <= 1 {
		return position, speed
	}
	mid := len(position) / 2
	lowPos, lowSpd := sortByPosition(position[:mid], speed[:mid])
	highPos, highSpd := sortByPosition(position[mid:], speed[mid:])
	resPos := make([]int, len(position))
	resSpd := make([]int, len(speed))
	l, r := 0, 0
	for i := range len(resPos) {
		if l >= len(lowPos) {
			resPos[i] = highPos[r]
			resSpd[i] = highSpd[r]
			r++
		} else if r >= len(highPos) {
			resPos[i] = lowPos[l]
			resSpd[i] = lowSpd[l]
			l++
		} else {
			if lowPos[l] < highPos[r] {
				resPos[i] = lowPos[l]
				resSpd[i] = lowSpd[l]
				l++
			} else {
				resPos[i] = highPos[r]
				resSpd[i] = highSpd[r]
				r++
			}
		}
	}
	return resPos, resSpd
}
