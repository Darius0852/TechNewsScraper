import requests
from bs4 import BeautifulSoup

# Set the URL to scrape
url = 'https://www.techcrunch.com/'
urlNew = ['https://www.wired.com', 'https://www.futurism.com', 'https://www.gizmodo.com', 'https://www.techcrunch.com/', 'https://www.nytimes.com/section/technology']

# Make a request to the website
response = requests.get(url, timeout=100)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the articles on the page
articles = soup.find_all('article')

# Print the title and summary of each article
for article in articles:
    title = article.h3.text
    summary = article.p.text
    print(f'{title}\n{summary}\n\n')
