package main

import (
	"fmt"
)

func main() {
	var num1, num2, num3 int
	fmt.Println("Enter the first number: ")
	fmt.Scanln(&num1)
	fmt.Println("Enter the second number: ")
	fmt.Scanln(&num2)
	fmt.Println("Enter the third number: ")
	fmt.Scanln(&num3)

	if num1 > num3 && num1 > num2 {
		fmt.Println(num1, "is the largest number...")
	} else if num2 > num3 && num2 > num1 {
		fmt.Println(num2, "is the largest number...")
	} else if num3 > num1 && num3 > num2 {
		fmt.Println(num3, "is the largest number...")
	} else {
		fmt.Println("There is no single largest number...")
	}
}
