import requests
from bs4 import BeautifulSoup

# URL to scrape (e.g., Hacker News main page)
URL = "https://news.ycombinator.com/"

def get_hacker_news_titles():
    """
    Parses and prints titles from the Hacker News homepage.
    """
    try:
        response = requests.get(URL)
        response.raise_for_status() # Check for HTTP errors

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all title lines by their CSS selector
        # On Hacker News, titles are in <td> tags with class 'title'
        # Inside them is an <a> tag
        title_lines = soup.select('tr.athing .titleline > a')

        if not title_lines:
            print("Titles not found. The website structure may have changed.")
            return

        print(f"--- Found {len(title_lines)} titles on Hacker News ---")
        for index, title in enumerate(title_lines):
            print(f"{index + 1}. {title.get_text()}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")

if __name__ == "__main__":
    get_hacker_news_titles()
