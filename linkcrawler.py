import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to crawl links on a webpage and return unique links
def crawl_unique_links(url):
    unique_links = set()  # Set to store unique links

    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags (links) in the HTML
        links = soup.find_all('a')

        # Extract and add the href attribute of each link to the set
        for link in links:
            href = link.get('href')
            if href:
                # Join relative URLs with the base URL to get absolute URLs
                absolute_url = urljoin(url, href)
                unique_links.add(absolute_url)

    except Exception as e:
        print(f"An error occurred: {e}")

    return unique_links

# Check if the script is called with a target URL argument
if len(sys.argv) != 2:
    print("Usage: python crawl_links.py <target_url>")
    sys.exit(1)

# Get the target URL from the command-line argument
website_url = sys.argv[1]

# Call the crawl_unique_links function with the provided website URL
unique_links = crawl_unique_links(website_url)

# Print the unique links
for link in unique_links:
    print(link)
