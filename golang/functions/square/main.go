package main

import "fmt"

func square(x *float64) {
	*x = *x * *x
}

func main() {
	x := 1.5
	fmt.Println(x)
	square(&x)
	fmt.Println(x)
}
