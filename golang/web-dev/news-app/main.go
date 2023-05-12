package main

import (
  "fmt"
  "net/http"
  "os"
  "log"
  "html/template"
  "net/url"
  "time"

  "cmd/news-api/"
  "github.com/joho/godotenv"
)

var tpl = template.Must(template.ParseFiles("index.html"))

//the {w} parameter is the structure we use to send responses to an HTTP request.
func indexHandler(w http.ResponseWriter, r *http.Request) {
  tpl.Execute(w, nil)
}

func searchHandler(w http.ResponseWriter, r *http.Request) {
  u, err := url.Parse(r.URL.String())
  if err != nil {
    http.Error(w, err.Error(), http.StatusInternalServerError)
    return
  }

  params := u.Query()
  searchQuery := params.Get("q")
  page := params.Get("page")
  if page == "" {
    page = "1"
  }

  fmt.Println("Search Query is: ", searchQuery)
  fmt.Println("Page is: ", page)
}

func main() {
  err := godotenv.Load()
  if err != nil {
    log.Println("Error loading .env file")
  }

  port := os.Getenv("PORT")
  if port == "" {
    port = "8080"
  }

  fs := http.FileServer(http.Dir("assets"))

  //this method is used to create an HTTP request multiplexer
  mux := http.NewServeMux()   
  mux.Handle("/assets/", http.StripPrefix("/assets/", fs))
  mux.HandleFunc("/", indexHandler)
  mux.HandleFunc("/search", searchHandler)

  //{http.ListenAndServe()} method which starts the server on the port defined in the port variable.
  http.ListenAndServe(":"+port, mux)
}

