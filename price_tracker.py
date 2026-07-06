import requests
import re
from bs4 import BeautifulSoup as bs
import urls
import components as cp

# Track the prices of components for my epic-mega-server shai-hulud
# Check prices on Amazon, Newegg, and eBay

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def get_newegg_price(url):
    # set the newegg url
    url =  urls.urls[0]["newegg_url"]

    # make the http request and print status
    response = requests.get(url, headers=headers, timeout=10)
    print(response.status_code)
    
    # pass the content to bs to parse
    soup = bs(response.text, "html.parser")
    span = soup.find("div", class_="price-current")
    if span:
        span_text = span.get_text()
    else:
        print("price div not found")
    
    match = re.search(r'\d+\.\d+', span_text)
    if match:
        price = float(match.group())
    newegg_price = cp.cpu["Newegg Price"] = price
    return newegg_price

get_newegg_price(urls.urls[0]["newegg_url"])
print(cp.cpu)
