import requests as r
from bs4 import BeautifulSoup
import urllib


def find_first_link(url):
    resp = r.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.title)

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    article_link = None

    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://zh.wikipedia.org/', article_link)

    return first_link
