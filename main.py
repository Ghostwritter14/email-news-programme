import requests

from send_email import send_email

# api key and url from new api
api_key = "0e2e91403ee74df68e5440a9dd665bf2"
url = "https://newsapi.org/v2/everything?" \
      "q=apple&" \
      "from=2023-04-10&to=2023-04-" \
      "10&sortBy=popularity&api" \
      "Key=0e2e91403ee74df68e5440a9dd665bf2" \
      "&language=en"

# making  the request
request = requests.get(url)

# get a dictionary of data
content = request.json()

# access the article titles with description
body = ""
for article in content["articles"][:10]:
    if article["title"] is not None:
        source_name = article['source']['Name'] if article['source'] is not None else 'Unknown Source'
        article_str = f"Subject: Recent News on Apple\n{article['title']}\n{source_name}\n{article['url']}\n\n"
        body += article_str

# send email and to avoid error encode in utf8
body = body.encode("utf-8")
send_email(message=body)

