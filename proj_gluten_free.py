# finding all links - without scrolling the whole page downwards
# by Pirjo 1/2020

import requests
import csv
from bs4 import BeautifulSoup
import re
from proj_scrape_item import scrape_item
from dict_to_csv import write_to_csv

url_temp = "https://www.foodie.fi/products/search2/gluteeniton?page={}&sort_order=relevancy&sort_dir=desc&main_view=1"

pages = range(1,21)
url_list_all = []
link_list = []
product_list= []

for page in pages:
    print("Fetching page number {} of 21".format(page))
    url = url_temp.format(page)
    url_list_all.append(url)
    response = requests.get(url)
    html_code = response.text
    soup_1 = BeautifulSoup(html_code, "html.parser")
    item_link = soup_1.find_all("a", {"class":"js-link-item"})
    for link in item_link:
        href_plain = link.get("href")
        href_ready = "https://www.foodie.fi" + href_plain
        item_info = scrape_item(href_ready)
        product_list.append(item_info)
        print(item_info)


dict_names = ["product", "ean", "unitprice", "country"]
write_to_csv("gluten_day5.csv", dict_names, product_list)
print("ready")
