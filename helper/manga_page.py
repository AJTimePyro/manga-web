#!/usr/bin/env python3


### Importing Modules, Files, etc...
from helper.chapter import *


### Getting Page info
class ChapterPage(CommonThings):

    def __init__(self, chapter_id):
        """
        Object initialising
        chapter_id - int
        """

        self.chapID = chapter_id
        super().__init__()    # Inheriting CommonThings class
        self.getPageUrl()
    
    def getPageUrl(self):
        """
        Getting Url of all pages of requested chapters
        """
        self.requestToWeb(f'https://api.mangaowl.to/v1/chapters/{self.chapID}/images')

        jsonData = json.loads(self.webcontent)
        resultData = jsonData['results']
        imgList = dict()
        count = 0

        for data in resultData:
            count += 1
            imgList[count] = data['image']
        self.pageList = json.dumps(imgList)

