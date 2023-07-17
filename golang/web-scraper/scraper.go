package main

import (
	"encoding/csv"
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"os"

	"github.com/gocolly/colly"
)

type PokemonProduct struct {
	URL   string `json:"url"`
	Name  string `json:"name"`
	Price string `json:"price"`
	Image string `json:"image"`
}

func main() {
	url := flag.String("url", "https://scrapeme.live/shop/page/1/", "URL to scrap.")
	selector := flag.String("selector", "a[href]", "custom CSS selectors.")
	allPages := flag.Bool("all", false, "Follow all pages of products.")
	/* 	depth := flag.Int("depth", 1, "Depth of the scrapping.")
	 */format := flag.String("format", "csv", "Select the output format (CSV or JSON).")

	flag.Parse()

	scrap(*url, *selector, *format, *allPages)
}

func scrap(url, selector, format string, follow bool) {
	var pokemonProducts []PokemonProduct
	var visitedUrls []string

	c := colly.NewCollector()

	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL)
	})

	c.OnError(func(_ *colly.Response, err error) {
		log.Println("Something went wrong:", err)
	})

	c.OnResponse(func(r *colly.Response) {
		fmt.Println("Visited", r.Request.URL)
	})

	c.OnScraped(func(r *colly.Response) {
		fmt.Println("Finished", r.Request.URL)
	})

	c.OnHTML("li.product", func(e *colly.HTMLElement) {
		pokemonProduct := PokemonProduct{}

		pokemonProduct.URL = e.ChildAttr("a", "href")
		pokemonProduct.Image = e.ChildAttr("img", "src")
		pokemonProduct.Name = e.ChildText("h2")
		pokemonProduct.Price = e.ChildText(".price")

		pokemonProducts = append(pokemonProducts, pokemonProduct)
	})

	if follow {
		c.OnHTML(selector, func(e *colly.HTMLElement) {
			link := e.Attr("href")
			fmt.Printf("Link found: %q -> %s\n", e.Text, link)

			for _, address := range visitedUrls {
				if link != address {
					c.Visit(link)
				}
			}

			visitedUrls = append(visitedUrls, link)
		})
	}

	c.Visit(url)

	switch format {
	case "csv", "CSV":
		if err := writeCSV(pokemonProducts); err != nil {
			log.Fatalln("Failed to create CSV", err)
		}
		fmt.Println("products.csv created!")
	case "JSON", "json":
		if err := writeJSON(pokemonProducts); err != nil {
			log.Fatalln("Failed to create JSON", err)
		}
		fmt.Println("products.json created!")
	default:
		fmt.Println("Invalid format!!")
	}
}

func writeCSV(pokemonProducts []PokemonProduct) error {
	file, err := os.Create("products.csv")
	if err != nil {
		return err
	}
	defer file.Close()

	writer := csv.NewWriter(file)

	headers := []string{
		"url",
		"image",
		"name",
		"price",
	}

	writer.Write(headers)

	for _, pokemonProduct := range pokemonProducts {
		record := []string{
			pokemonProduct.URL,
			pokemonProduct.Image,
			pokemonProduct.Name,
			pokemonProduct.Price,
		}

		writer.Write(record)
		defer writer.Flush()

	}
	return nil
}

func writeJSON(pokemonProducts []PokemonProduct) error {
	file, err := os.Create("products.json")
	if err != nil {
		return err
	}
	defer file.Close()

	writer := json.NewEncoder(file)
	writer.SetIndent("", "  ")

	if err := writer.Encode(pokemonProducts); err != nil {
		return err
	}

	return nil
}
