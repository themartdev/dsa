package medium

func findDuplicate(nums []int) int {
	slow, fast := nums[0], nums[nums[0]]
	for slow != fast {
		slow = nums[slow]
		fast = nums[nums[fast]]
	}

	fast = 0
	for fast != slow {
		fast = nums[fast]
		slow = nums[slow]
	}
	return slow
}
