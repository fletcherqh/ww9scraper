from random import randint
from bs4 import BeautifulSoup
import requests
import argparse
import sys
import urllib.request


def mainPage(url): #will get list of every chapter from the main page

    site = requests.get(url)

    soup = BeautifulSoup(site.content, 'html.parser')

    myList = soup.findAll('a', attrs={'class':'text md:text-lg font-bold mb-1 text-text-normal'})

    if not args.chapter: #Will go through all chapters in order, then ask if you want to view. type stop to break loop
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
        print("Looking for selected chapter...")
        for i in myList[::-1]:
            
            subUrl = i['href']
            
            #if subUrl == "https://ww9.readonepiece.com/chapter/one-piece-chapter-" + args.chapter:
            if subUrl == "https://ww2.readkaguyasama.com/chapter/kaguya-sama-love-is-war-chapter-" + args.chapter:

                print(f"Found chapter {args.chapter}!")
                
                subPage(subUrl)
                sys.exit(1)
            
        print(f"Could not find chapter {args.chapter}")



def subPage(url): #gets every image from the sub-page

    site = requests.get(url)

    soup = BeautifulSoup(site.content, 'html.parser')

    myList = soup.findAll('img', attrs={'class':'mb-3 mx-auto js-page'})

    print('Getting images...')
    
    pagenum = 0
    for i in myList:
        pagenum += 1
        image_url = i['src']
        print(image_url)

        img_data = requests.get(image_url).content
        with open(f'../../Desktop/Comics/page{pagenum}.jpg', 'wb') as handler:
            handler.write(img_data)


if __name__ == "__main__":

    gui.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
    
    parser = argparse.ArgumentParser(description='Download all images of a chapter from ww9')
    parser.add_argument('-c', '--chapter', help='Specific chapter to download. Format: [00X, 0XX, XXX, XXXX]')
    args = parser.parse_args()
    
    ww2url = "https://ww2.readkaguyasama.com/manga/kaguya-sama-love-is-war/"
    ww9url = "https://ww9.readonepiece.com/manga/one-piece/"
    mainPage(ww2url)
