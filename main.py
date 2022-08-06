from random import randint
from bs4 import BeautifulSoup
import requests


def mainPage(url): #will get list of every chapter from the main page

    site = requests.get(url)

    soup = BeautifulSoup(site.content, 'html.parser')

    myList = soup.findAll('a', attrs={'class':'text md:text-lg font-bold mb-1 text-text-normal'})

    chapterNum = str(input("What chapter would you like to read? (type ALL to view all in order)\n"))


    if chapterNum == "ALL": #Will go through all chapters in order, then ask if you want to view. type stop to break loop
        for i in myList[::-1]:
            
            subUrl = i['href']
            
            print(subUrl)
            
            choice = input("view: y/n or stop\n")
            
            if choice == 'y':
                subPage(subUrl)
            if choice == 'stop':
                break
            else:
                continue

    
    else:  #allows you to pick a specific chapter
        for i in myList[::-1]:
            
            subUrl = i['href']
            
            if subUrl == "https://ww9.readonepiece.com/chapter/one-piece-chapter-" + chapterNum:

                print(subUrl)
                
                subPage(subUrl)



def subPage(url): #gets every image from the sub-page

    site = requests.get(url)

    soup = BeautifulSoup(site.content, 'html.parser')

    myList = soup.findAll('img', attrs={'class':'mb-3 mx-auto js-page'})
    
    for i in myList:
        print(i['src'])


if __name__ == "__main__":
    ww9url = "https://ww9.readonepiece.com/manga/one-piece/"
    mainPage(ww9url)
