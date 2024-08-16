package medium

// 5,6,|7,8,9,1,2|,3,4

func search(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l <= r {
		i := (l + r) / 2
		//fmt.Printf("l: %d, r: %d, i:%d\n", l, r, i)
		if nums[i] == target {
			return i
		}
		//asc := nums[moduloIndex(n, i-1)] < nums[i]
		if nums[i] >= nums[l] {
			if nums[i] >= target && nums[l] <= target {
				r = i - 1
			} else {
				l = i + 1
			}
		} else {
			if nums[i] <= target && nums[r] >= target {
				l = i + 1
			} else {
				r = i - 1
			}
		}
	}
	return -1
}
