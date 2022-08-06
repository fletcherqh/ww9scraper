from random import randint
from bs4 import BeautifulSoup
import requests


def mainPage(url):

    site = requests.get(url)

    soup = BeautifulSoup(site.content, 'html.parser')

    myList = soup.findAll('a', attrs={'class':'text md:text-lg font-bold mb-1 text-text-normal'})

    for i in myList[::-1]:
        subUrl = i['href']

        subPage(subUrl)

        input()


def subPage(url):
    print(url)

    site = requests.get(url)

    soup = BeautifulSoup(site.content, 'html.parser')

    myList = soup.findAll('img', attrs={'class':'mb-3 mx-auto js-page'})
    
    for i in myList:
        print(i['src'])



ww9url = "https://ww9.readonepiece.com/manga/one-piece/"
mainPage(ww9url)
