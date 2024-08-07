package main

import (
	"fmt"
	"github.com/simon-martineau/dsa/internal/alg"
	"unicode/utf8"
)

func main() {
	// var d rune = '9'
	// var i byte = byte(d)
	// asChar := rune(i)
	// fmt.Printf("%v", asChar)

	a := "ééta"
	b := "taéèa"
	c := alg.SortedLetters(b)
	fmt.Printf("sorted: %s\n", c)
	anag := alg.IsAnagram(a, b)
	fmt.Printf("IsAnagram: %v\n", anag)
	count := utf8.RuneCount([]byte(a))
	fmt.Printf("rune count: %d\n", count)
	fmt.Printf("len: %d\n", len(a))

	for i, val := range a {
		fmt.Printf("idx: %d, val: %c\n", i, val)
	}
}
