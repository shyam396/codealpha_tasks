import requests
from bs4 import BeautifulSoup
import csv

# Website to scrape (practice site)
url = "https://quotes.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract data
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Save to CSV
with open("quotes_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for quote, author in zip(quotes, authors):
        writer.writerow([quote.text, author.text])

print("✅ Data scraped successfully and saved as quotes_data.csv")
