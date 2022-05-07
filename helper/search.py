#!/usr/bin/env python3


### Importing Modules, Files, etc...
from helper.common import *
import random
import os.path


### Search Engine
class SearchEngine(CommonThings):

    def __init__(self, query:str):
        self.query = query
        super().__init__()    # Inheriting CommonThings class
        self.removingSpace()
        self.searchingResult()
    
    def removingSpace(self):
        self.query = self.query.replace(' ', '_')

    def searchingResult(self):
        self.requestToWeb(f'https://mangakakalot.com/search/story/{self.query}')
        self.parsingData()
    
    def parsingData(self):
        mangaList = dict()
        count = 0
        for i in self.parsedData.find_all('div', class_='story_item'):
            count += 1
            url = i.a
            urlData = os.path.split(url['href'])[1]
            img = url.img
            mangaList[count] = {
                'title' : img['alt'],
                'url-data' : urlData,
                'img' : img['src']
            }
        self.mangaList = json.dumps(mangaList)



### Random Anime Gif Finder
class RandomAnimeGif(CommonThings):

    def __init__(self):
        super().__init__()    # Inheriting CommonThings class
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
        self.requestToWeb(
            f'https://api.waifu.pics/sfw/{self.category}',
            False
        )
        jsonData = json.loads(self.webcontent)
        self.imgUrl = jsonData['url']

