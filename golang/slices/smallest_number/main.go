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
  for i, j := range x {
    if j < smallest_num || i == 0 {
      smallest_num = j
    }
  }
  fmt.Println(smallest_num)
}
