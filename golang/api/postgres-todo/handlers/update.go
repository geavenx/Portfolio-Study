package handlers

import (
	"encoding/json"
	"log"
	"net/http"
	"strconv"

	"github.com/geavenx/api-postgres/models"
	"github.com/go-chi/chi/v5"
)

func Update(w http.ResponseWriter, r *http.Request) {
	id, err := strconv.Atoi(chi.URLParam(r, "id"))
	if err != nil {
		log.Printf("Error parsing id: %v", err)
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}

	var todo models.Todo
	err = json.NewDecoder(r.Body).Decode(&todo)
	if err != nil {
		log.Printf("Error on json decoding: %v", err)
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}

	rows, err := models.Update(int64(id), todo)
	if err != nil {
		log.Printf("Error updating entry: %v", err)
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}

	if rows > 1 {
		log.Printf("Error: %d entries updated", rows)
	}
	resp := map[string]any{
		"Error":   false,
		"Message": "Successfully updated entry!",
	}

	w.Header().Add("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resp)
}
