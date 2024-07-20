package main

import (
	"fmt"
	"github.com/simon-martineau/dsa/internal/sort"
	"math/rand"
	time2 "time"
)

func main() {
	arr := makeSlice(10_000_000)
	//fmt.Printf("Array: %v\n", arr)
	duration, arr := time(func() []int {
		return sort.QuickSort(arr)
	})

	sorted := isSorted(arr)
	//fmt.Printf("Array: %v\n", arr)
	fmt.Printf("Sorted: %v\n", sorted)
	fmt.Printf("Execution took %v ms", duration.Milliseconds())
}

func time[T any](exec func() T) (time2.Duration, T) {
	start := time2.Now()
	res := exec()
	return time2.Since(start), res
}

func isSorted(arr []int) bool {
	for i := 0; i < len(arr)-1; i++ {
		if arr[i] > arr[i+1] {
			return false
		}
	}
	return true
}

func makeSlice(length int) []int {
	arr := make([]int, length)
	for i := range arr {
		arr[i] = rand.Intn(length)
	}
	return arr
}
