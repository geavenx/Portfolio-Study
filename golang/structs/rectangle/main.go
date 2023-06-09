package main

import (
	"fmt"
	"math"
)

type Rectangle struct {
	x1, y1, x2, y2 float64
}

func distance(x1, x2, y1, y2 float64) float64 {
	a := x2 - x1
	b := y2 - y1
	return math.Sqrt(a*a + b*b)
}

func (n *Rectangle) area() float64 {
	length := distance(n.x1, n.y1, n.x1, n.y2)
	width := distance(n.x1, n.y1, n.x2, n.y1)

	return width * length
}

func main() {
	n := Rectangle{0, 0, 10, 10}
	fmt.Println(n.area())
}
