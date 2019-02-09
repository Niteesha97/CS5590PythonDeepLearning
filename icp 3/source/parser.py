from html.parser import HTMLParser
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
class TitleParser(HTMLParser):
    def _init_(self):
        HTMLParser._init_(self)
        self.match = False
        self.title = ''
    def handle_starttag(self, tag, attributes):
        self.match = True if tag == 'title' else False
    def handle_data(self, data):
        if self.match:
            self.title = data
            self.match = False
url = "https://en.wikipedia.org/wiki/Deep_learning"


html_string = str(urlopen(url).read())
parser = TitleParser()
parser.feed(html_string)
print(parser.title)


def getlinks(url):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, 'html.parser')
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
    return links
print(getlinks("https://en.wikipedia.org/wiki/Deep_learning"))