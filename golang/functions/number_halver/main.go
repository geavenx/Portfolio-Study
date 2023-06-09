package main

import "fmt"

func half(n int) (x float32, y bool) {
	nf := float32(n)
	x = nf / 2.0
	if n%2 == 0 {
		y = true
	} else {
		y = false
	}
	return
}

func main() {
	fmt.Println(half(86))
}
