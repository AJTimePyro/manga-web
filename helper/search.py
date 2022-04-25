#!/usr/bin/env python3


### Importing Modules, Files, etc...
from urllib import request as req
from bs4 import BeautifulSoup
import random
import json


### Common data
class commonThings:

    def __init__(self):
        self.headers = {
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }


### Search Engine
class SearchEngine(commonThings):

    def __init__(self, query:str):
        self.query = query
        commonThings.__init__(self)
        self.removingSpace()
        self.searchingResult()
    
    def removingSpace(self):
        self.query = self.query.replace(' ', '_')

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
        self.mangaList = json.dumps(mangaList)



### Random Anime Gif Finder
class RandomAnimeGif(commonThings):

    def __init__(self):
        commonThings.__init__(self)
        self.preDefine = [
            "waifu",
            "neko",
            "shinobu",
            "megumin",
            "bully",
            "cuddle",
            "cry",
            "hug",
            "awoo",
            "kiss",
            "lick",
            "pat",
            "smug",
            "bonk",
            "yeet",
            "blush",
            "smile",
            "wave",
            "highfive",
            "handhold",
            "nom",
            "bite",
            "glomp",
            "slap",
            "kill",
            "kick",
            "happy",
            "wink",
            "poke",
            "dance",
            "cringe"
        ]
        self.selectingRandomCategory()
    
    def selectingRandomCategory(self):
        self.category = random.choice(self.preDefine)
        self.searchGif()
    
    def searchGif(self):
        requesting = req.Request(
            f'https://api.waifu.pics/sfw/{self.category}',
            headers = self.headers
        )
        res = req.urlopen(requesting)
        data = res.read()
        jsonData = json.loads(data)
        self.imgUrl = jsonData['url']

