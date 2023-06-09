package main

import "fmt"

func makeEvenGenerator() func() int {
	i := 0
	return func() (ret int) {
		ret = i
		i += 2
		return
	}
}

func makeOddGenerator() func() int {
	i := 1
	return func() (ret int) {
		ret = i
		i += 2
		return
	}
}

func main() {
	nextOdd := makeOddGenerator()
	fmt.Println(nextOdd()) // 0 (or 1 if odd)
	fmt.Println(nextOdd()) // 2 (or 3 if odd)
	fmt.Println(nextOdd()) // 4 (or 5 if odd)
	// ...
}
