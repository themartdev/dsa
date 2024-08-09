package main

import (
	"errors"
	"sort"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	var res [][]int
	found := make(map[string]struct{})
	for i := 0; i < len(nums)-2; i++ {
		target := 0 - nums[i]
		low, high := i+1, len(nums)-1
		val, err := _twoSum(nums, low, high, target)
		if err == nil {
			triplet := []int{nums[val[0]], nums[val[1]], nums[i]}
			sort.Ints(triplet)
			hash := hashTriplet(triplet)
			_, present := found[hash]
			if !present {
				found[hash] = struct{}{}
				res = append(res, triplet)
			}
		}
	}
	return res
}

func hashTriplet(triplet []int) string {
	return string(triplet[0]) + string(triplet[1]) + string(triplet[2])
}

func _twoSum(numbers []int, low, high, target int) ([]int, error) {
	for high > low {
		total := numbers[low] + numbers[high]

		if total == target {
			return []int{low, high}, nil
		} else if total > target {
			high--
		} else {
			low++
		}
	}

	return nil, errors.New("cannot find twoSum")
}
