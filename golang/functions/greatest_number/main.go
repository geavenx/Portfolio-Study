package main

import "fmt"

func greatest(list ...int) int {
	n := 0
	for _, v := range list {
		if v > n {
			n = v
		}
	}
	return n
}

func main() {
	res := greatest(1, 2, 4, 5, 6, 55, 34)
	fmt.Println(res)
}
