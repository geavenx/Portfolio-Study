package main

import "fmt"

func main() {
  fmt.Println("Enter Fahrenheit temperature: ")
  var fh float32
  fmt.Scanf("%f", &fh)
  
  celsius := (fh - 32) * 5 / 9
  fmt.Println("Temperature in Celsius: ", celsius)
}
