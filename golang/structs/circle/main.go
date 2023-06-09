package main

import (
	"fmt"
	"math"
)

type Circle struct {
	x float64
	y float64
	r float64
}

func circleArea(z *Circle) float64 {
	return math.Pi * z.r * z.r
}

func main() {
	c := Circle{0, 0, 5}
	fmt.Println(circleArea(&c))
}
