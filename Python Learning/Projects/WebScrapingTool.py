import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Print debug information
    print(f"Status Code: {response.status_code}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and display article titles
        articles = soup.find_all('h2', class_='article-title')
        print(f"Number of Articles Found: {len(articles)}")

        for index, article in enumerate(articles, start=1):
            title = article.text.strip()
            print(f"{index}. {title}")

    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":
    # Replace this URL with the actual URL of a news website
    news_url = "https://www.bbc.com/news"
    scrape_news(news_url)
