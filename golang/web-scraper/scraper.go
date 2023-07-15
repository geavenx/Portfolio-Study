package main

import (
	"encoding/csv"
	"flag"
	"fmt"
	"log"
	"os"

	"github.com/gocolly/colly"
)

type PokemonProduct struct {
	url   string
	image string
	name  string
	price string
}

func main() {
	url := flag.String("url", "https://scrapeme.live/shop/page/1/", "URL to scrap.")
	selector := flag.String("selector", "li.product", "custom CSS selectors.")
	allPages := flag.Bool("all", false, "Follow all pages of products.")

	flag.Parse()

	scrap(*url, *selector, *allPages)
}

func scrap(url, selector string, follow bool) {
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

	c.OnHTML(selector, func(e *colly.HTMLElement) {
		pokemonProduct := PokemonProduct{}

		pokemonProduct.url = e.ChildAttr("a", "href")
		pokemonProduct.image = e.ChildAttr("img", "src")
		pokemonProduct.name = e.ChildText("h2")
		pokemonProduct.price = e.ChildText(".price")

		pokemonProducts = append(pokemonProducts, pokemonProduct)
	})

	if follow {
		c.OnHTML("a.page-numbers[href]", func(e *colly.HTMLElement) {
			link := e.Attr("href")
			fmt.Printf("Link found: %q -> %s\n", e.Text, link)

			for _, address := range visitedUrls {
				if link != address {
					c.Visit(link)
				} /* else {
					fmt.Println("Link already scrapped, ignoring...")
				} */
			}

			visitedUrls = append(visitedUrls, link)
		})
	}

	c.Visit(url)

	file, err := os.Create("products.csv")
	if err != nil {
		log.Fatalln("Failed to create csv", err)
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
			pokemonProduct.url,
			pokemonProduct.image,
			pokemonProduct.name,
			pokemonProduct.price,
		}

		writer.Write(record)
		defer writer.Flush()
	}
}
