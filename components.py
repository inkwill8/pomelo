from enum import Enum


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
        self.amzn_price = None

    def set_amzn_price(self, price):
        self.amzn_price = price
        
    def set_newegg_price(self, price):
        self.newegg_price = price

    def set_bb_price(self, price):
        self.bb_price = price
