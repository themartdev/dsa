package main

import "fmt"

// koko loves to eat bananas. there are n piles of bananas, the ith pile has piles[i] bananas. the guards have gone and will come back in h hours.
//
// koko can decide her bananas-per-hour eating speed of k. each hour, she chooses some pile of bananas and eats k bananas from that pile. if the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
//
// koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
//
// return the minimum integer k such that she can eat all the bananas within h hours.

// [3,6,7,11], h=8
// 0,3,4,8 = 15 - (3*4) = 3
// 0,2,3,7 = 12 - (4*4) = -4
// 0, 1, 2, 6 = 9
// 0, 0, 1, 5 = 6
// 0, 0, 0, 5 = 5
// k = 4

func minEatingSpeed(piles []int, h int) int {
	maxVal := 0
	for _, val := range piles {
		maxVal = max(maxVal, val)
	}
	// l is the highest bad guess, r is the lowest good guess
	l, r := -1, (maxVal*len(piles))+1
	fmt.Printf("l,r = %d,%d\n", l, r)
	for r-l > 1 {
		k := (l + r) / 2
		fmt.Printf("k=%d\n", k)
		res := testK(piles, h, k)
		if res {
			r = k
		} else {
			l = k
		}
	}
	return r
}

func testK(piles []int, h, k int) bool {
	epoch := 0
	for _, val := range piles {
		res := val / k
		if val%k != 0 {
			res++
		}
		epoch += res
	}
	fmt.Printf("Testing k=%d, epoch=%d\n", k, epoch)
	return epoch <= h
}
