package handlers

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/geavenx/ccValidator/models"
)

func Get(rw http.ResponseWriter, r *http.Request) {
	var cardNum models.Card

	err := json.NewDecoder(r.Body).Decode(&cardNum)
	if err != nil {
		log.Printf("Error decoding JSON: %v", err)
		http.Error(rw, http.StatusText(http.StatusBadRequest), http.StatusBadRequest)
		return
	}
	if cardNum.Cc == "" {
		http.Error(rw, "Invalid JSON body", http.StatusBadRequest)
		return
	}

	validator, err := models.CcValid(cardNum.Cc)
	cardNetwork, err2 := models.CheckNetwork(cardNum.Cc)

	var resp map[string]any

	if err != nil {
		resp = map[string]any{
			"Error":   true,
			"Message": fmt.Sprintf("An error has ocurred when trying to validade the card: %v", err),
		}
	} else if err2 != nil {
		resp = map[string]any{
			"Error":   true,
			"Message": fmt.Sprintf("An error has ocurred when trying to validade the card network: %v", err2),
		}
	} else {
		resp = map[string]any{
			"Error":        false,
			"Card Status":  fmt.Sprint(validator),
			"Card Network": fmt.Sprint(cardNetwork),
		}
	}

	rw.Header().Add("Content-Type", "application/json")
	json.NewEncoder(rw).Encode(resp)
}
