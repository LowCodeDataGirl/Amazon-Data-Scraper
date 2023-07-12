# Amazon-Data-Scraper

This repository contains two Python scripts (`app.py` and `app(2).py`) that perform web scraping on HTML files and convert the extracted data to JSON and CSV formats. These scripts utilize the `json`, `os`, and `BeautifulSoup` libraries.

## Files

1. `csv_output.csv`: This file is the output of the `app.py` script. It contains the scraped data from a single HTML file in CSV format.

2. `json_output.json`: This file is the output of the `app(2).py` script. It contains the scraped data from multiple HTML files in JSON format.

3. `app.py`: This Python script performs web scraping on a single HTML file (`index.html`) and extracts specific information such as the image link, title, rating, and price of a product. The scraped data is then saved to a JSON file (`data.json`).

4. `app(2).py`: This Python script performs web scraping on multiple HTML files stored in the `Pages Snapshots` directory. It extracts similar information to that in `app.py` from each file and saves the scraped data to a JSON file (`all_data.json`).

## Prerequisites

- Python 3.x
- `json` library
- `os` library
- `BeautifulSoup` library

## Usage

1. Ensure that you have Python 3.x installed on your system.
2. Install the required libraries by running the following command:
   ```shell
   pip install beautifulsoup4
   ```
3. Run the `app.py` script to perform web scraping on the `index.html` file and save the data to a JSON file (`data.json`).
   ```shell
   python app.py
   ```
4. Place the HTML files you want to scrape in the `Pages Snapshots` directory for the `app(2).py` script.
5. Run the `app(2).py` script to perform web scraping on the HTML files and save the data to a JSON file (`all_data.json`).
   ```shell
   python app(2).py
   ```

## Output

- After running `app.py`, the scraped data from the `index.html` file will be saved as `data.json`.

- After running `app(2).py`, the scraped data from the HTML files in the `Pages Snapshots` directory will be saved as `all_data.json`.

- The `data.json` and `all_data.json` files can be further processed or used as desired.
