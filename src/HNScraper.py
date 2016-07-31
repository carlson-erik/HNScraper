from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

def readConfig(config_file):
    return config_file

# Simple function to pull down the html from the web servers
def pullHTML(url):
    try:
        html = urlopen(url)
        return html
    except HTTPError as e:
        print("FAILURE:" + e)
        return None

def getPostLink(html):
    return html

def getPostPoints(html):
    return html

# Main function to clean up script
def main():
    url = "http://news.ycombinator.com/news?p=" + str(1) + ".html"
    current_html = pullHTML(url)
    #bsObj = BeautifulSoup(current_html, "html.parser")
    print(current_html)
    return True

main()
