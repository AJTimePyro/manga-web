#!/usr/bin/env python3


### Importing Modules, Files, etc...
from helper.common import *
import random


### Search Engine
class SearchEngine(CommonThings):

    def __init__(self, query:str):
        self.query = query
        super().__init__()    # Inheriting CommonThings class
        self.removingSpace()
        self.searchingResult()
    
    def removingSpace(self):
        """
        Replacing space with %20 for searching query
        """
        self.query = self.query.replace(' ', '%20')

    def searchingResult(self):
        """
        Searching Query and getting proper results
        """
        self.requestToWeb(f'https://api.mangaowl.to/v1/search?q={self.query}')
        self.parsingData()
    
    def parsingData(self):
        """
        Getting useful data
        """
        jsonData = json.loads(self.webcontent)
        resultData = jsonData['results']

        if resultData:  # If data exist
            mangaList = dict()
            count = 0
            for data in resultData:
                count += 1
                mangaList[count] = {
                    'title' : data['name'],
                    'url-data' : data['slug'],
                    'img' : data['thumbnail']
                }
            self.mangaList = json.dumps(mangaList)
        else:   # If data not exist
            self.mangaList = None


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
        self.requestToWeb(f'https://api.waifu.pics/sfw/{self.category}')
        jsonData = json.loads(self.webcontent)
        self.imgUrl = jsonData['url']

