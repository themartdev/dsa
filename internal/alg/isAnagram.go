package alg

import "sort"

func SortedLetters(w string) string {
	r := []rune(w)
	sort.Slice(r, func(i, j int) bool {
		return r[i] < r[j]
	})
	return string(r)
}

func IsAnagram(a string, b string) bool {
	available := make(map[rune]int)

	for _, val := range a {
		available[val]++
	}

	for _, val := range b {
		n, ok := available[val]
		if !ok {
			return false
		}
		n--
		if n > 0 {
			available[val] = n
		} else {
			delete(available, val)
		}
	}

	return len(available) == 0
}
