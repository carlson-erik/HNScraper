from urllib.request import urlopen
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
        keywords.append(config['Keywords'][key])
    return keywords

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
    keywords = readConfig()
    print(keywords)

main()
