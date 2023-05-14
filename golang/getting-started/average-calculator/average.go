package main

import (
	"fmt"
)

func main() {
	var total, sum, average, x int
	fmt.Println("Input numbers of elements: ")
	fmt.Scanln(&total)
	for i := 0; i < total; i++ {
		fmt.Println("Input Element: ")
		fmt.Scanln(&x)
		sum += x
	}
	average = sum / total
	fmt.Println("Your average is: ", average)
}
