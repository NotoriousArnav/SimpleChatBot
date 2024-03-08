from langchain_community.tools import BaseTool
import bs4
import requests

# TODO: Add Support for Medium and sites like that
class PageText(BaseTool):
    name="scrape_article"
    description = "Get Text Content of Any Article using its URL."    

    def _run(self, url) -> str:
        response = requests.get(
                url,
                timeout=60,
                allow_redirects=True
            )
        soup = bs4.BeautifulSoup(response.content)
        return soup.text