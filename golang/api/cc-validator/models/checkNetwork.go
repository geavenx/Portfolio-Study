package models

func CheckNetwork(cc string) (network string, err error) {
	for index, n := range cc {
		if index == 0 {
			if err != nil {
				panic("An error has ocurred [ CheckNetwork() ]")
			}
			strn := int(n - '0')
			switch strn {
			case 3:
				return "American Express", err
			case 4:
				return "Visa", err
			case 5:
				return "Master Card", err
			case 6:
				return "Discover", err
			default:
				return "Card network not found", err
			}
		}
	}
	return
}
