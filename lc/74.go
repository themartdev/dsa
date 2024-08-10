package main

//You are given an m x n integer matrix matrix with the following two properties:
//
//Each row is sorted in non-decreasing order.
//The first integer of each row is greater than the last integer of the previous row.
//Given an integer target, return true if target is in matrix or false otherwise.
//
//You must write a solution in O(log(m * n)) time complexity.
//
//

func searchMatrix(matrix [][]int, target int) bool {
	l, r := 0, len(matrix)-1
	for l <= r {
		i := (l + r) / 2
		low, high := matrix[i][0], matrix[i][len(matrix[i])-1]
		if target < low {
			r = r - 1
		} else if target > high {
			l = l + 1
		} else {
			return binSearch(matrix[i], target)
		}
	}
	return false
}

// 11, 14, 20, 24, 43
func binSearch(nums []int, target int) bool {
	l, r := 0, len(nums)-1

	for l <= r {
		i := (l + r) / 2
		if nums[i] < target {
			l = i + 1
		} else if nums[i] > target {
			r = i - 1
		} else {
			return true
		}
	}
	return false
}
