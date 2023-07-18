package handlers

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/geavenx/api-postgres/models"
)

func List(w http.ResponseWriter, r *http.Request) {
	todos, err := models.GetAll()
	if err != nil {
		log.Printf("Error getting entries: %v", err)
	}
	w.Header().Add("Content-Type", "application/json")
	json.NewEncoder(w).Encode(todos)
}
