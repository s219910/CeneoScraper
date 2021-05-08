import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ceneo.pl/71299209#tab=reviews")

page_dom = BeautifulSoup(response.text,'html.parser')


#print(page_dom.prettify()))


reviews = page_dom.select("div.js_product-review")
print(type(reviews))
review = reviews.pop(0)
print(type(review))

reviews = page_dom.select_one("div.js_product-review")
print(type(review))


review_id = review["data-entry-id"]
author = review.select_one("span.user-post__author-name").text.strip()
recommendation = review.select_one(
    "span.user-post__author-recomendation").text.strip()
stars = 
content = 
pros = review.select("div.review-feature__title--positives ~ div.review-feature__item")
cons = review.select("div.review-feature__title--negatives ~ div.review-feature__item")
useful = review.select_one("button.vote-yes")


#dokończ pozostałe


