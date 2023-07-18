package handlers

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/geavenx/api-postgres/models"
)

func Create(w http.ResponseWriter, r *http.Request) {
	var todo models.Todo

	err := json.NewDecoder(r.Body).Decode(&todo)
	if err != nil {
		log.Printf("Error json decoding: %v", err)
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}
	id, err := models.Insert(todo)

	var resp map[string]any

	if err != nil {
		resp = map[string]any{
			"Error":   true,
			"Message": fmt.Sprintf("An error has ocurred when trying to Insert(): %v", err),
		}

	} else {
		resp = map[string]any{
			"Error":   false,
			"Message": fmt.Sprintf("Successfully inserted! ID: %v", id),
		}
	}

	w.Header().Add("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resp)
}
