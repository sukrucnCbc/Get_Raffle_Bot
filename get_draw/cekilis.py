from ast import keyword
from pyexpat.errors import messages
from turtle import st
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


ytLiveChatURL="https://www.youtube.com/live_chat?continuation=0ofMyAN-Gl5DaWtxSndvWVZVTlRTalJuYTFaRE5rNXlka2xKT0hWdGVuUm1NRTkzRWd0cVprdG1VR1o1U2xKa2F4b1Q2cWpkdVFFTkNndHFaa3RtVUdaNVNsSmtheUFCTUFBJTNEMAGCAQYIBBgCIACIAQGgAa--v--57IIDqAEAsgEA"
keyword="what"
eligibleUsers=set()

 # start web browser
browser=webdriver.Firefox()
def getHTML(url):  

    # get source code
    browser.get(url)
    time.sleep(2)
    page_source = browser.page_source
   
    return page_source

def parseHtml(html_source):
    return BeautifulSoup(html_source, 'html.parser')

def getMessages(soup):
    return soup.find_all("yt-live-chat-text-message-renderer")


def updateEligibleUsers(messages):
    
    global eligibleUsers

    for message in messages:
        content=message.find("div", {"id":"content"})
        author=content.find("span", {"id":"author-name"}).text
        message_content=content.find("span", {"id":"message"}).text

        if keyword in message_content.lower():
            eligibleUsers.add(author)
    return eligibleUsers        

def startDrawing(eligibleUsersList):
    global eligibleUsers

    print("Cekilis Baslıyor! {totalUserCount} kisi katıldı".format(totalUserCount=len(eligibleUsers)))

    for i in range(1,5):
        dots=i * "."
        print("Rastgele bir sayı çekiliyor"+dots)
        time.sleep(1)
    print("Hazır mısınız?")

    eligibleUsersList=list(eligibleUsers)
    print("{totalUserCount} kişi arasından Kazanan: ".format(
        totalUserCount=len(eligibleUsersList)),random.choice(eligibleUsersList))

def main(): 
    for i in range(0,7):
        html_source=getHTML(ytLiveChatURL)
        soup=parseHtml(html_source)
        messages=getMessages(soup)
        eligibleUsers=updateEligibleUsers(messages)
        print("{count} kişi katıldı".format(count=len(eligibleUsers)))
        time.sleep(2)

    eligibleUsersList=list(eligibleUsers)
    startDrawing(eligibleUsersList)
    browser.close()

main()