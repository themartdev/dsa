package medium

/*
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
*/

func characterReplacement(s string, k int) int {
	count := make(map[byte]int)
	left, res, maxFrequency := 0, 0, 0

	for right := 0; right < len(s); right++ {
		char := s[right]
		count[char] += 1
		maxFrequency = max(maxFrequency, count[char])
		nReplacements := right - left + 1 - maxFrequency
		if nReplacements > k {
			count[s[left]] -= 1
			left++
		}
		res = max(res, right-left+1)
	}
	return res
}

// A B B B
