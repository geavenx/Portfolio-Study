package main

import (
	"fmt"
	"math"
)

type Circle struct {
	x, y, r float64
}

type Rectangle struct {
	x1, y1, x2, y2 float64
}

type Shape interface {
	area() float64
	perimeter() float64
}

// AREA DO CIRCULO
func (c *Circle) area() float64 {
	return math.Pi * c.r * c.r
}

// PERIMETRO DO CIRCULO
func (c *Circle) perimeter() float64 {
	return 2 * math.Pi * c.r
}

// LADOS DO RETANGULO
func distance(x1, y1, x2, y2 float64) float64 {
	a := x2 - x1
	b := y1 - y2
	return math.Sqrt(a*a + b*b)
}

// AREA DO RETANGULO
func (r *Rectangle) area() float64 {
	length := distance(r.x1, r.y1, r.x1, r.y2)
	width := distance(r.x1, r.y1, r.x2, r.y1)
	return length * width
}

// PERIMETRO DO RETANGULO
func (r *Rectangle) perimeter() float64 {
	length := distance(r.x1, r.y1, r.x1, r.y2)
	width := distance(r.x1, r.y1, r.x2, r.y1)
	return 2 * (width + length)
}

// AREA TOTAL
func totalArea(circles ...Circle) float64 {
	var total float64
	for _, c := range circles {
		total += c.area()
	}
	return total
}

func main() {
	c := &Circle{0, 0, 5}
	re := &Rectangle{0, 0, 13.124, 17.54}
	fmt.Println("circle area(): ", c.area(), "m²")
	fmt.Println("circle perimeter(): ", c.perimeter(), "m")
	fmt.Println("rectangle area(): ", re.area(), "m²")
	fmt.Println("rectangle perimeter(): ", re.perimeter(), "m")
}
