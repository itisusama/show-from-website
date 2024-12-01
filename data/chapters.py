import requests
from bs4 import BeautifulSoup

# URL of the page
url = "https://www.booksie.com/739870-trapped-in-the-frame"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all divs with the specified class
    target_divs = soup.find_all('div', class_='column read_list_right pb-0')
    
    # Check if any divs were found
    if target_divs:
        for idx, div in enumerate(target_divs, start=1):
            # Find the <strong> and <i> tags within the div
            strong_tag = div.find('strong')
            italic_tag = div.find('i')
            
            # Extract and print the text between the tags if both exist
            if strong_tag and italic_tag:
                print("----------")
                print(f"Chapter Name: {strong_tag.text}")
                print(f"Chapter Data: {italic_tag.text}\n")
                print("----------")
            else:
                print(f"Div {idx}: Missing <strong> or <i> tags.\n")
    else:
        print("No divs with the specified class found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
