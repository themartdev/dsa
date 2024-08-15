package medium

import "fmt"

// Return true if one of s1's permutations is the substring of s2

// adc
// d c o d a
func checkInclusion(s1, s2 string) bool {
	bank := make(map[byte]int)
	total := 0
	for i := 0; i < len(s1); i++ {
		bank[s1[i]] += 1
		total++
	}

	left := 0
	for right := 0; right < len(s2); {
		fmt.Printf("bank: %v, left: %d, right: %d\n", bank, left, right)
		letter := s2[right]
		if bank[letter] > 0 {
			bank[letter]--
			total--
			right++
		} else {
			if right != left {
				bank[s2[left]]++
				total++
				left++
			} else {
				right++
				left++
			}
		}

		if total == 0 {
			return true
		}
	}
	return false
}
