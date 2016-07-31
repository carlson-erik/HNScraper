import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys
import configparser

# Reads in the local configuration file
def readConfig():
    config = configparser.ConfigParser()
    config.read("config.cfg")
    keywords = []
    for key in config["Keywords"]:
        keywords.append(config['Keywords'][key].lower())
    return keywords

# Simple function to pull down the html from the web servers
def pullHTML(url):
    try:
        html = 0
        with urllib.request.urlopen(url) as response:
            html = response.read()
        return html
    except HTTPError as e:
        print(e)
        return None

def getAllPosts(bsoup_html):
    return bsoup_html

def getPostLink(bsoup_html):
    return bsoup_html

def getPostPoints(bsoup_html):
    return bsoup_html

# Main function to clean up script
def main():
    keywords = readConfig()
    url = "https://news.ycombinator.com/news?p=" + str(1) + ".html"
    print("KEYWORDS FOR SCAN:")
    print(keywords)
    current_html = pullHTML(url)
    bsoup_html = BeautifulSoup(current_html, "html.parser")
    print(bsoup_html)

main()
