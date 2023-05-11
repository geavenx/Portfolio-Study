package main

import (
  "net/http"
  "fmt"
  "time"
  "html/template"
)

//Create a struct that holds information to be displayed in our HTML file
type Welcome struct {
  Name string
  Time string
}

//Go application entrypoint
func main() {
  welcome := Welcome{"Anonymous", time.Now().Format(time.Stamp)}

  templates := template.Must(template.ParseFiles("/home/vitor/go/src/first-web-test/template/index.html"))

  http.Handle("/static/",
    http.StripPrefix("/static/",
      http.FileServer(http.Dir("static"))))

  http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    
    if name := r.FormValue("Name"); name != "" {
        welcome.Name = name;
      }
    
    if err := templates.ExecuteTemplate(w, "index.html", welcome); err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
      }
  })

  fmt.Println("Listening");
  fmt.Println(http.ListenAndServe(":8080", nil));
}
