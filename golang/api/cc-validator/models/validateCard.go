package models

import (
	"strconv"
)

func CcValid(cardNumber string) (valid string, err error) {
	validator := 0
	for index, n := range cardNumber {
		strn := string(n)
		intn, err := strconv.Atoi(strn)

		if err != nil {
			panic("An error has ocurred [ CcValid() ]")
		}

		if index%2 == 0 {
			intn = intn * 2

			if intn >= 10 {
				x := intn % 10
				y := intn / 10
				intn = x + y
			}
		}
		validator = validator + intn
	}
	if validator%10 == 0 {
		valid := "valid"
		return valid, err
	} else {
		valid := "invalid"
		return valid, err
	}
}
