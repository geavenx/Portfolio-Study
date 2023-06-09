package main

import "fmt"

func main() {
  fmt.Println("Enter distance in feets: ")
  var feets float32
  fmt.Scanf("%f", &feets)

  meters := feets * 0.3048
  fmt.Println("Distance in meters: ", meters)
}
