import json
from bs4 import BeautifulSoup

# Read the html file
with open("index.html", "r") as f:
    html_content = f.read()

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with the specific class
divs = soup.find_all("div", class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16")

# Initialize an empty list to hold all items
items = []

for div in divs:
    item = {}

    try:
        link = div.find("img", class_="s-image")['src']
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
    except:
        rating = ' '
    item['rating'] = rating

    try:
        price = div.find("span", class_="a-price-whole").text
    except:
        price = ' '
    item['price'] = price

    items.append(item)

# Write to a json file
with open('data.json', 'w') as f:
    json.dump(items, f)
