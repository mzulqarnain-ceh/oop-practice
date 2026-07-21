import os
import csv
import requests
from bs4 import BeautifulSoup
folder=os.path.dirname(__file__)
path=os.path.join(folder,"scrap_quotes.csv")
# fetching url function
def fetch_html(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        else:
            print(f"Failed to load page. response status code is: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network related error {e}")
        return None
def parse_quotes(html):
    soup=BeautifulSoup(html,"html.parser")
    parse_data=[]
    # Finding quotes elements
    quote_element=soup.find_all("div", class_="quote")
    for element in quote_element:
        text=element.find("span",class_="text").text
        author=element.find("small",class_="author").text
        tags_element=element.find_all("a",class_="tag")
        tags=[tag.text for tag in tags_element]
        quote_dict={
            "text":text,
            "author":author,
            "tags":tags,
        }
        parse_data.append(quote_dict)
    return parse_data
def display_quotes(quotes):
    print("\n....Scraped Quotes.....\n")
    for i,quote in enumerate(quotes):
        tags_string=", ".join(quote["tags"])
        print(f"{i+1} - {quote['text']}")
        print(f"    -{quote['author']} | Tags: {tags_string} \n")
    print(f"Total extracted Quotes: {len(quotes)}")
def save_to_csv(quotes):
    with open(path,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(["Quotes","Author","Tags"])
        for quote in quotes:
            tags_string=", ".join(quote["tags"])
            writer.writerow([quote["text"],quote["author"],tags_string])
    print(f"Data successfully saved to path: {path}")
if __name__=="__main__":
    url="http://quotes.toscrape.com/"
    print(f"Scraping data from {url}........")
    html=fetch_html(url)
    if html:
        quotes=parse_quotes(html)
        display_quotes(quotes)
        save_to_csv(quotes)
    else:
        print("Failed to fetch page.")