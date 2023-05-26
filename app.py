import os
import json
from bs4 import BeautifulSoup

# Directory where the HTML files are stored
dir_path = r"C:\Users\Peace Paix\Documents\Web Scraping\Amazon Web Scraping\Pages Snapshots"

# Initialize an empty list to hold all items
all_items = []

# Iterate over every file in the directory with name 'pageX.html'
for i in range(1, 76):  # This will go from page1.html to page75.html
    file_name = f'page{i}.html'
    
    # Full file path
    file_path = os.path.join(dir_path, file_name)
    
    if os.path.isfile(file_path):
        # Read the html file
        with open(file_path, "r", encoding='utf-8') as f:
            html_content = f.read()

        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all divs with the specific class
        divs = soup.find_all("div", class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16")

        for div in divs:
            item = {}

            try:
                link = div.find("img", class_="s-image")['src']
                link = link.split('/')[-1]
            except:
                link = ' '
            item['link'] = link

            try:
                title = div.find("span", class_="a-size-medium a-color-base a-text-normal").text
            except:
                title = ' '
            item['title'] = title

            try:
                rating = div.find("span", class_="a-icon-alt").text
                rating = float(rating.split()[0])
            except:
                rating = ' '
            item['rating'] = rating

            try:
                price = div.find("span", class_="a-price-whole").text
                price = float(price.replace(",", ""))
            except:
                price = ' '
            item['price'] = price

            all_items.append(item)

# Write to a single json file
with open(f'{dir_path}\\all_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_items, f)
