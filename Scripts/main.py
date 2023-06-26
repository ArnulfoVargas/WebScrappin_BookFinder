import requests
import bs4


url = "http://books.toscrape.com/catalogue/page-{}.html"
good_books = []

for i in range(1, 50):
    req = requests.get(url.format(i))
    soup = bs4.BeautifulSoup(req.text, 'lxml')

    page_books = soup.select(".product_pod")

    for book in page_books:
        rate = book.select(".star-rating")[0]["class"][1]
        if rate == "Four" or rate == "Five":
            good_books.append( book.select('a')[1]["title"])


for book in good_books:
    print(book)
