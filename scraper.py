from bs4 import BeautifulSoup
import requests
import csv

def get_page(url):
    html_tag = requests.get(url)

    if html_tag.status_code == 200:
        return BeautifulSoup(html_tag.text, 'lxml')
    else:
        raise Exception(f"Page not found! Status code: {html_tag.status_code}")
def extract_book_data(tag):
    rating = tag.find('p', class_ = 'star-rating')['class'][1]
    title = tag.h3.a["title"]
    price = tag.find("p", class_ = "price_color").text.replace('Â',' ')
    data = {
        "rating": rating,
        "title":title,
        "price":price
    }
    return data
def parce_books(soup):
    books = []
    tags = soup.find_all("article", class_ = "product_pod")
    for tag in tags:
        data = extract_book_data(tag)
        if data:
            books.append(data)
    return books
def save_to_csv(books, filename = "books.csv"):
    headers = books[0].keys()
    with open(filename, mode="w") as file:
         writer = csv.DictWriter(file, fieldnames=headers)
         writer.writeheader()
         writer.writerows(books)
    print(f"{len(books)} number of books saved to {filename}")


def main():
    soup = get_page("https://books.toscrape.com")
    books = parce_books(soup)
    

    for index, book in enumerate(books):
        print("\n")
        print(f"{index+1}-{book['title']}:{book['price']}, star rating: {book['rating']}/Five")

    save_to_csv(books)

if __name__ == "__main__":
    main()