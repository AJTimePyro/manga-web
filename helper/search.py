#!/usr/bin/env python3


### Importing Modules, Files, etc.
from urllib import request as req
from bs4 import BeautifulSoup


### Search Engine
class SearchEngine:

    def __init__(self, query):
        self.query = query
        self.headers = {
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        self.searchingResult()
    
    def searchingResult(self):
        requesting = req.Request(
            f'https://mangakakalot.com/search/story/{self.query}',
            headers = self.headers
        )
        res = req.urlopen(requesting)
        self.webcontent = res.read()
        self.parsingData()
    
    def parsingData(self):
        page = BeautifulSoup(self.webcontent, 'html.parser')
        mangaList = list()
        for i in page.find_all('div', class_='story_item'):
            url = i.a
            mangaList.append((url['href'], url.img['src']))
        print(mangaList)

