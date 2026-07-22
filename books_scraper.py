import os
import csv
import requests
from bs4 import BeautifulSoup
folder=os.path.dirname(__file__)
path=os.path.join(folder,"books_scraping.csv")
def fetch_html(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        else:
            print(f"Failed to load page with status code error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error! Network related error {e}")
        return None
def parse_books(html):
    soup=BeautifulSoup(html,"html.parser")
    parse_data=[]
    book_element=soup.find_all("article",class_="product_pod")
    for element in book_element:
        title=element.find("h3").find("a")["title"]
        price=element.find("p",class_="price_color").text
        availability=element.find("p",class_="instock availability").text.strip()
        rating_tag=element.find("p",class_="star-rating")
        rating=rating_tag["class"][1]
        book_dict={
            "title":title,
            "price":price,
            "availability":availability,
            "rating":rating
        }
        parse_data.append(book_dict)
    return parse_data
def display_books(books):
    print("\n.....Scraped Books.....\n")
    for i,book in enumerate(books):
        print(f"{i+1} - {book["title"]} | Price: {book["price"]} | Availability: {book["availability"]} | Rating: {book["rating"]}")
    print(f"Total no of scraped books: {len(books)}")
def save_to_csv(books):
    with open(path,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(["Book Title","Price","Availability","Rating"])
        for book in books:
            writer.writerow([book["title"],book["price"],book["availability"],book["rating"]])
    print(f"Data Successfully saved to {path}")
# entry Point
if __name__=="__main__":
    url="http://books.toscrape.com/"
    print(f"Scraping data from: {url}...")
    html=fetch_html(url)
    if html:
        books=parse_books(html)
        display_books(books)
        save_to_csv(books)
    else:
        print("Failed to fetch page.")
