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

# Pulls down the html from the web servers
def pullHTML(url):
    try:
        html = 0
        with urllib.request.urlopen(url) as response:
            html = response.read()
        return html
    except HTTPError as e:
        print(e)
        return None

# Check to see if the title contains any of the keywords
def checkLinkTitle(title, keywords):
    for keyword in keywords:
        if keyword in title:
            return True
    return False

# Scans the doc, pulls the table of posts out and stores each post's link in the array
def buildAllPosts(bsoup_html, keywords):
    ret_list = []
    for post in bsoup_html.findAll("a", {"class" : "storylink"}):
        if checkLinkTitle(post.get_text().lower(), keywords) == True:
            cur_string = post.get_text() + " -- " + str(post['href'])
            ret_list.append(cur_string)
    return ret_list

# Main function to clean up script
def main():
    keywords = readConfig()
    for page_num in range(1, 40):
        print("--------------------------------------- Page " + str(page_num) + " ---------------------------------------")
        url = "https://news.ycombinator.com/news?p=" + str(page_num)
        current_html = pullHTML(url)
        bsoup_html = BeautifulSoup(current_html, "html.parser")
        all_posts = buildAllPosts(bsoup_html, keywords)
        for post in all_posts:
            print(post)
        print("--------------------------------------- Page " + str(page_num) + " ---------------------------------------")

main()
