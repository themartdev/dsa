package main

import (
	"regexp"
	"strings"
)

func main() {

}

func isPalindrome(s string) bool {
	s = preprocess(s)
	l := len(s)
	if l <= 1 {
		return true
	}

	// If length is not even, ignore middle character
	even := l/2 == 0
	if !even {
		left, right := s[:l/2], s[l/2+1:]
		s = left + right
	}
	l = len(s)

	for offset := 0; offset < l/2; offset++ {
		if s[0+offset] != s[len(s)-1-offset] {
			return false
		}
	}
	return true
}

var alphaNumRegex = regexp.MustCompile(`[^a-zA-Z0-9]+`)

func preprocess(s string) string {
	s = strings.ToLower(s)
	return alphaNumRegex.ReplaceAllString(s, "")
}
