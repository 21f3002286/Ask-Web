import requests
from bs4 import BeautifulSoup
from newspaper import Article

# This function is a backup scraper if newspaper3k fails
def fallback_scraper(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            content = ""

            for p in paragraphs:
                content += p.get_text() + "\n"

            if soup.title:
                title = soup.title.string.strip()
            else:
                title = "No title found"

            return title, url, content
        else:
            print("Failed to fetch the page:", response.status_code)
            return None
    except Exception as e:
        print("Error in fallback_scraper for URL:", url)
        print("Error message:", str(e))
        return None

# Main function to scrape text
def text_scraper(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.title, url, article.text
    except Exception as e:
        print("newspaper3k could not scrape:", url)
        print("Trying fallback method...")
        return fallback_scraper(url)