from bs4 import BeautifulSoup
import requests
import sys
import os
from tkinter import *

def mainPage(url, chapter): #will get list of every chapter from the main page
    site = requests.get(url)

    soup = BeautifulSoup(site.content, 'html.parser')

    myList = soup.findAll('a', attrs={'class':'text md:text-lg font-bold mb-1 text-text-normal'})
    myList = (myList[::-1]) #reverse list from bottom to top and enumerate

    #change chapter number to new format
    if int(chapter) < 0:
        chapter = ""
    elif int(chapter) < 10:
        chapter = "00" + str(chapter)
    elif int(chapter) < 100:
        chapter = "0" + str(chapter)
    else:
        chapter = chapter

    if chapter == "": #Will go through all chapters in order, then ask if you want to view. type stop to break loop
        for i in myList:
            
            subUrl = i['href']
            
            print(subUrl)
            
            choice = input("view: y/n or stop\n")
            
            if choice == 'y':
                subPage(subUrl)
                sys.exit(1)
            if choice == 'stop':
                break
            else:
                continue

    
    else:  #allows you to pick a specific chapter
        print("Looking for selected chapter...")
        
        for i in myList[int(chapter)-1:]:
            
            subUrl = i['href']
            
            if subUrl == "https://ww9.readonepiece.com/chapter/one-piece-chapter-" + chapter:

                print(f"Found chapter {chapter}!")
                
                subPage(subUrl)
                sys.exit(1)
            
        print(f"Could not find chapter {chapter}")



def subPage(url): #gets every image from the sub-page

    site = requests.get(url)

    soup = BeautifulSoup(site.content, 'html.parser')

    myList = soup.findAll('img', attrs={'class':'mb-3 mx-auto js-page'})

    try:
        filePath = f"{path}/Chapter {chapter}"
        os.mkdir(filePath) #make a directory here
    except:
        print('File path not found')
        sys.exit(1)

    print('Getting images...')

    pagenum = 0
    for i in myList:
        pagenum += 1
        image_url = i['src']
        print(image_url)

        img_data = requests.get(image_url).content
        with open(f'{filePath}/page{pagenum}.jpg', 'wb') as handler:
            handler.write(img_data)

#def binarySearch(arr, left, right, chapter): not being used
#    #base case
#    if right >= left:
# 
#        mid = left + (right - left) // 2
# 
#        if arr[mid]['href'] == chapter:
#            return arr[mid]
# 
#        elif arr[mid]['href'] > chapter:
#            return binarySearch(arr, left, mid-1, chapter)
# 
#        else:
#            return binarySearch(arr, mid+1, right, chapter)
# 
#    else: #if element not in array
#        return -1

if __name__ == "__main__":
    
    ww9url = "https://ww9.readonepiece.com/manga/one-piece/"

    def getGUI():
        global e
        global chapter
        global path
        path = path_entry.get()
        chapter = chapter_entry.get()
        root.destroy()

    root = Tk()

    root.geometry("300x100")
    root.title('Chapter Selection')
    
    path_label = Label(root, text = 'Path', font=('calibre',10, 'bold'))
    path_entry = Entry(root)
    path_entry.focus_set()

    chapter_label = Label(root, text = 'Chapter', font=('calibre',10, 'bold'))
    chapter_entry = Entry(root)
    chapter_entry.focus_set()

    button1 = Button(root,text='enter',command=getGUI)

    path_label.grid(row=0,column=1)
    path_entry.grid(row=0,column=2)
    chapter_label.grid(row=1,column=1)
    chapter_entry.grid(row=1,column=2)
    button1.grid(row=2,column=2)

    root.mainloop()

    if path == '':
        print("please add path")
        sys.exit(1)
    if chapter == '':
        chapter = -1

    mainPage(ww9url, chapter)
