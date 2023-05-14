package main

import (
	"fmt"
)

func main() {
	var n, n1 int
	fmt.Print("Enter the number: ")
	fmt.Scan(&n)
	for i := 1; i < 11; i++ {
		n1 = n * i
		fmt.Println(n, "X", i, "=", n1)
	}
}

