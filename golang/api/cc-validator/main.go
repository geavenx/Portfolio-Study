package main

import (
	"net/http"

	"github.com/geavenx/ccValidator/handlers"
	"github.com/go-chi/chi/v5"
)

func main() {
	r := chi.NewRouter()

	r.Get("/", handlers.Get)

	http.ListenAndServe(":8080", r)
}
