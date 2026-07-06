import re
from enum import Enum

import requests
from bs4 import BeautifulSoup as bs


class ComponentType(Enum):
    cpu = "CPU"
    ram = "RAM"
    cooler = "CPU Cooler"
    ssd = "SSD"
    gpu = "GPU"
    mobo = "Motherboard"
    psu = "Power Supply"
    hdd = "HDD"
    fan = "Fan"


class Component:
    def __init__(self, name: str, url: str, type: ComponentType):
        self.name = name
        self.url = url
        self.type = type

        # prices are set to none initially and will be updated later on after web scraping
        self.amzn_price = None
        self.newegg_price = None
        self.bb_price = None

    # Setters
    def set_amzn_price(self, price):
        self.amzn_price = price

    def set_newegg_price(self, price):
        self.newegg_price = price

    def set_bb_price(self, price):
        self.bb_price = price

    # Instance Methods
    def get_newegg_price(self, url, headers):
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

        match = re.search(r"\d+\.\d+", span_text)
        if match:
            price = float(match.group())
        return price
