package main

//func main() {
//	res := findMin([]int{2, 1})
//	fmt.Printf("result: %v", res)
//}

// Solution is more complicated than it could/should be, we can just keep searching until l==r and exit then

func findMin(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	l, r := 0, len(nums)-1
	//fmt.Printf("l,r := %v,%v\n", l, r)
	for {
		i := (l + r) / 2
		if nums[circularIndex(len(nums), i-1)] > nums[i] {
			return nums[i]
		} else if nums[circularIndex(len(nums), i+1)] < nums[i] {
			return nums[circularIndex(len(nums), i+1)]
		} else if nums[i] > nums[r] {
			l = i
		} else if nums[i] < nums[r] {
			r = i
		}
	}
}

func circularIndex(length, i int) int {
	if i < 0 {
		i += length
	}
	return i
}

// 4,5,6,7,8,9,1,2,3,
