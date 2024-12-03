import requests
from bs4 import BeautifulSoup
import json

# URL of the website
url = "https://www.booksie.com/portfolio-view/thritter-297135"

# Send a GET request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Check for request errors

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Define the specific class to search for
target_class = "text-center padd-left5 is-centered has-text-centered cover-box"

# Find all div elements with the target class
divs = soup.find_all('div', class_=target_class)

# Prepare a list to store books data
books = []

# Extract only href, alt, and src attributes
for div in divs:
    link_tag = div.find('a', href=True)  # Find <a> tag with href attribute
    img_tag = div.find('img', alt=True, src=True)  # Find <img> tag with alt and src attributes
    
    # Extract attributes if they exist
    href = link_tag['href'] if link_tag else None
    alt = img_tag['alt'] if img_tag else None
    src = img_tag['data-src'] if img_tag else None

    # Append the data to the books list as a dictionary
    books.append({
        "link": href,
        "name": alt,
        "image": src
    })

# Save the books data to a JSON file
with open('data/books.json', 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=4)

print("Books data saved to books.json")
