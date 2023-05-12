package main

import (
  "net/http"
  "os"
  "log"
  "html/template"
  "net/url"
  "strconv"
  "time"
  "bytes"
  "math"

  "github.com/geavenx/newsApi"
  "github.com/joho/godotenv"
)

var tpl = template.Must(template.ParseFiles("index.html"))

type Search struct {
  Query      string
  NextPage   int
  TotalPages int
  Results    *newsApi.Results
}

func (s *Search) IsLastPage() bool {
        return s.NextPage >= s.TotalPages
}

func (s *Search) CurrentPage() int {
        if s.NextPage == 1 {
          return s.NextPage
        }

        return s.NextPage -1
}

func (s *Search) PreviousPage() int {
        return s.CurrentPage() - 1
  }

//the {w} parameter is the structure we use to send responses to an HTTP request.
func indexHandler(w http.ResponseWriter, r *http.Request) {
  tpl.Execute(w, nil)
}

func searchHandler(newsapi *newsApi.Client) http.HandlerFunc {
  return func(w http.ResponseWriter, r *http.Request) {
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

  results, err := newsapi.FetchEverything(searchQuery, page)
  if err != nil {
      http.Error(w, err.Error(), http.StatusInternalServerError)
      return
    }

  nextPage, err := strconv.Atoi(page)
    if err != nil {
      http.Error(w, err.Error(), http.StatusInternalServerError)
      return
  }
  
    search := &Search{
      Query: searchQuery,
      NextPage: nextPage,
      TotalPages: int(math.Ceil(float64(results.TotalResults) / float64(newsapi.PageSize))),
      Results: results,
  }

    if ok := !search.IsLastPage(); ok {
      search.NextPage++
    }

  buf := &bytes.Buffer{}
  err = tpl.Execute(buf, search)
  if err != nil {
      http.Error(w, err.Error(), http.StatusInternalServerError)
      return
  }

    buf.WriteTo(w)
  }
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
  
  apikey := os.Getenv("NEWS_API_KEY")
  if apikey == "" {
    log.Fatal("Env: apikey must be set")
  }

  myClient := &http.Client{Timeout: 10 * time.Second}
  newsapi := newsApi.NewClient(myClient, apikey, 20)

  fs := http.FileServer(http.Dir("assets"))

  //this method is used to create an HTTP request multiplexer
  mux := http.NewServeMux()   
  mux.Handle("/assets/", http.StripPrefix("/assets/", fs))
  
  mux.HandleFunc("/", indexHandler)
    mux.HandleFunc("/search", searchHandler(newsapi))

  //{http.ListenAndServe()} method which starts the server on the port defined in the port variable.
  http.ListenAndServe(":"+port, mux)
}

