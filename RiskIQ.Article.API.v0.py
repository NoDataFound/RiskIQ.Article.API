#!/usr/bin/env python
# -*- coding: utf-8 -*-

#RiskIQ script to extract IoC's from articles.
#API Documentation: https://api.riskiq.net/api/articles/
#author__ = 'Cory Kennedy (cory@riskiq.com)'
#version__ = '1.0.0'
import requests
import ujson as json
import sys
from datetime import datetime

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    IGREEN ='\033[92m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    PURPLE = '\033[1;35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print("")
print(style.YELLOW+"Note: Below values can be found here: https://community.riskiq.com/settings")
print (style.BLACK+"----------------------------------------------------------------")
username = input(style.GREEN+'Enter your https://community.riskiq.com email address: ')
key = input(style.CYAN+'Enter your https://community.riskiq.com API key: ')
headers = {'Content-Type': 'application/json'}

def all_articles():
    r = requests.get('https://api.riskiq.net/pt/v2/articles', headers=headers, auth=(username, key))
    data = r.json()
    for article in data['articles']:
        print (style.BLACK+"---"+style.GREEN+"GUID"+style.BLACK+"-----------------"+style.CYAN+"TITLE"+style.BLACK+"--------------")
        print (style.GREEN+article['guid'], style.BLACK+"| "+style.CYAN+article['title'])
        print (style.BLACK+"-------------------------------------------")
        print (style.YELLOW+"TAGS: ")
        for tag in article['tags']:
            print ("   " +style.WHITE+tag)
        print ("")  


def guid_articles():
    guid = input(style.GREEN+'Enter Article GUID: ')
    url = ('https://api.riskiq.net/pt/v2/articles/indicators?articleGuid=' + guid)
    r = requests.get(url,  headers=headers, auth=(username, key))
    data = r.json()
    for indicators in data['indicators']:
        print (style.GREEN+indicators['type'], "," + style.CYAN+indicators['value'])
        print ("")  
        
 
def show_menu():
    print("")
    print (style.CYAN+"  +----------------------------------------------------------------+")
    print (style.CYAN+"""  |   .______       __       _______. __  ___  __    ______        | 
  |   |   _  \     |  |     /       ||  |/  / |  |  /  __  \       |
  |   |  |_)  |    |  |    |   (----`|  '  /  |  | |  |  |  |      |
  |   |      /     |  |     \   \    |    <   |  | |  |  |  |      |  
  |   |  |\  \----.|  | .----)   |   |  .  \  |  | |  `--'  '--.   |
  |   | _| `._____||__| |_______/    |__|\__\ |__|  \_____\_API_|  |""")
    print (style.CYAN+"  |",style.MAGENTA+"                           https://api.riskiq.net/api/articles",style.CYAN+"|")                         
    print (style.CYAN+"  +----------------------------------------------------------------+")
    print(style.RESET)
    r = requests.get('https://api.riskiq.net/pt/v2/articles', headers=headers, auth=(username, key))
    data = r.json()
    print("Here are our latest articles: ")
    for article in data['articles'][:5]:
        print (style.BLACK+"---"+style.GREEN+"GUID"+style.BLACK+"---------------------------------------------------------------"+style.BLUE+"TITLE"+style.BLACK+"--------------------------------------------------")
        print (style.GREEN+article['guid'], style.BLACK+"| "+style.CYAN+article['title'])
    print (style.BLACK+"-----------------------------------------------------------------------------------------------------------------------------")
    print ("")
    print (style.BLUE+"1) List all RiskIQ TIP Article "+ style.RESET + style.GREEN+ "GUIDs" + style.RESET +", " + style.CYAN+ "Titles" + style.BLUE + " and " + style.RESET + style.WHITE+"TAGS")
    print (style.CYAN+"2) Get all indicators from a single article GUID")
    print(style.RESET)
    print (style.GREEN+"Q) Exit\n")
    print(style.RESET)
 
def menu():
    while True:
        show_menu()
        choice = input('Enter your choice: ').lower()
        print ("")
        if choice == '1':
            all_articles()
        elif choice == '2':
            guid_articles()        
        elif choice == 'q':
            return
        else:
            print(f'Hmmm: <{choice}>,try again, or dont. Whatever')
 
if __name__ == '__main__':
    menu()