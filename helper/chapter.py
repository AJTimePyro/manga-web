#!/usr/bin/env python3


### Importing Modules, Files, etc...
from helper.common import *


### Getting a List of Chapters
class Chapter(CommonThings):

    def __init__(self, manga_id, single_url=False):
        self.mangaID = manga_id
        self.single_url = single_url
        super().__init__()    # Inheriting CommonThings class
        self.gettingChapters()
        
    
    def gettingChapters(self):
        """
        Getting Chapters name and id
        """
        self.requestToWeb(f'https://api.mangaowl.to/v1/stories/{self.mangaID}')
        
        jsonData = json.loads(self.webcontent)
        self.title = jsonData['name']
        self.posterUrl = jsonData['thumbnail']
        resultData = jsonData['chapters']
        
        chapterList = dict()
        count = 0

        for data in resultData:
            count += 1
            chapterList[count] = {
                'chapter-title' : data['name'],
                'chapter-id' : data['id']
            }
        self.chapJson = json.dumps(chapterList)
