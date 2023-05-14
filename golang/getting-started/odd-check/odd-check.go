package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Println("Enter your number: ")
	fmt.Scanln(&n)
	if n%2 == 0 {
		fmt.Println(n, "is even...")
	} else {
		fmt.Println(n, "is odd...")
	}
}
