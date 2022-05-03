#!/usr/bin/env python3


### Importing Modules, Files, etc...
# from helper.common import *
from helper.common import *


### Getting a List of Chapters
class Chapter(commonThings):

    def __init__(self, manga_id):
        self.mangaID = manga_id
        self.chapterList = dict()
        commonThings.__init__(self)
        self.gettingChapters()
        self.chapJson = json.dumps(self.chapterList)
    
    def gettingChapters(self):
        if 'manga-' in self.mangaID:
            self.url = 'https://readmanganato.com/'
            self.readmanganato()
        else:
            self.url = 'https://mangakakalot.com/'
            if 'read-' not in self.mangaID:
                self.url = f'{self.url}/manga/'
            self.mangakakalot()

    def readmanganato(self):
        self.__request()
        count = 0

        # For finding Title of manga
        self.titleClass = self.parsedData.find(class_ = 'story-info-right')
        self.__getTitleName()

        # For Getting Manga Poster
        self.posterClass = self.parsedData.find(class_ = 'info-image')
        self.__getMangaPoster()

        # Parsing Chapter List
        for i in self.parsedData.find_all('li', class_ = 'a-h'):
            count += 1
            tag = i.a
            url = tag['href']
            title = tag.text
            self.chapterList[count] = {
                'chapter-no' : title,
                'url' : url
            }

    def mangakakalot(self):
        self.__request()
        count = 0

        # For finding Title of manga
        self.titleClass = self.parsedData.find(class_ = 'manga-info-text')
        self.__getTitleName()

        # For Getting Manga Poster
        self.posterClass = self.parsedData.find(class_ = 'manga-info-pic')
        self.__getMangaPoster()

        # Parsing Chapter List
        for i in self.parsedData.find_all(class_ = 'row')[1:]:
            count += 1
            a_tag = i.span.a
            url = a_tag['href']
            title = a_tag.text
            self.chapterList[count] = {
                'chapter-no' : title,
                'url' : url
            }

    def __request(self):
        self.requestToWeb(f'{self.url}/{self.mangaID}')

    def __getTitleName(self):
        titleH1Tag = self.titleClass.h1
        self.title = titleH1Tag.text
    
    def __getMangaPoster(self):
        imgTag = self.posterClass.img
        self.posterUrl = imgTag['src']

