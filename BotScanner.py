import re
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# README: WIP you can find pages with interesting information by reading the robot.txt file of a site.
# This script reaches out to a site (or list of sites) and scans the pages that the owners don't want you to look at

def getEndpoints(url):
    endpoints = []
    robotTxt = requests.get(url + "/robots.txt").text

    #If the entry is listed as disallowed add it to the list of pages to scan
    for line in robotTxt.splitlines():
        if "Disallow" in line:
            # I'm using replace() because there's a space at the beginning of the filepath (urlparse(line)[2])
            # and it's screwing with my url creation
            endpoints.append(url + urlparse(line)[2].replace(" ", ""))

    return endpoints

def getData(url):
    if re.fullmatch("(https|http)://[a-zA-Z]+\.[a-zA-Z]+", url):
        endpoints = getEndpoints(url)

    else:
        raise Exception("Error: Invalid URL")

    for endpoint in endpoints:
        tempData = requests.get(endpoint).text
        analyzeData(tempData)

def analyzeData(data):
    secrets = []

    soup = BeautifulSoup(data)
    soup.find_all(string="key")

def scan(url):
    pass

scan("https://discoverdestiny.org")
#getEndpoints("https://discoverdestiny.org")