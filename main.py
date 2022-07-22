from random import randint
from bs4 import BeautifulSoup
import requests


def mainPage(url):

    site = requests.get(url)

    soup = BeautifulSoup(site.content, 'html.parser')

    myList = soup.findAll('a', attrs={'class':'text md:text-lg font-bold mb-1 text-text-normal'})

    for i in myList:
        subUrl = i['href']
        subPage(subUrl)


def subPage(url):
    
    site = requests.get(url)



ww9url = "https://ww9.readonepiece.com/manga/one-piece/"
MainPage(ww9url)
