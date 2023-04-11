import requests

# api key and url from new api
api_key = "0e2e91403ee74df68e5440a9dd665bf2"
url = "https://newsapi.org/v2/everything?q=apple&from=2023-04-10&to=2023-04-10&sortBy=popularity&apiKey=0e2e91403ee74df68e5440a9dd665bf2"

# making  the request
request = requests.get(url)

# get a dictionary of data
content = request.json()

# access the article titles with description
for article in content["articles"]:
    print(article["title"])

