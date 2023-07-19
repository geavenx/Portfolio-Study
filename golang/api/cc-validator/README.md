
# Credit Card Validator API

The API takes a JSON payload GET request with the credit card number, and returns if the credit card is valid or invalid and the identified card network


## What I learned?

- The Luhn Algorithm
- How runes work in Golang
- [Go-chi](https://github.com/go-chi/chi) for HTTP services
- To handle with multiple packages
- Better file organization


## Step-by-step
- Implement the Luhn algorithm
- Create an HTTP server
- Configure the server to respond to GET requests having a JSON payload
- Accept valid JSON requests and proceed to step 5, whilst rejecting invalid requests using an HTTP 400 status code
- Extract the credit card number from the JSON payload
- Run the Luhn algorithm on the number
- Wrap the result into a JSON response payload
- Return the payload back to the user through the HTTP server

