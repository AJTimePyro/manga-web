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

