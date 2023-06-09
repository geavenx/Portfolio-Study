package main

import "fmt"

func main() {
  x := []int{
  48,96,86,68,
  57,82,63,70,
  37,34,83,27,
  19,97, 9,17,
  }
  
  var smallest_num int
  for _, i := range x {
    if i < smallest_num {
      smallest_num := i
    }
  }
  fmt.Println(smallest_num)
}
