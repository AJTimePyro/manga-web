#!/usr/bin/env python3


### Importing Modules, Files, etc...
from helper.common import *
import re


### Getting a List of Chapters
class Chapter(commonThings):

    def __init__(self, manga_id, single_url=False):
        self.mangaID = manga_id
        self.single_url = single_url
        self.chapterList = dict()
        commonThings.__init__(self)
        self.gettingChapters()
        if not self.single_url:
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

        if not self.single_url:
            # For finding Title of manga
            self.titleClass = self.parsedData.find(class_ = 'story-info-right')
            self.__getTitleName()

            # For Getting Manga Poster
            self.posterClass = self.parsedData.find(class_ = 'info-image')
            self.__getMangaPoster()

        # Parsing Chapter List
        for i in self.parsedData.find_all('li', class_ = 'a-h'):
            tag = i.a
            url = tag['href']
            if not count and self.single_url:
                self.normUrl = url
                break
            chapID = re.search(r'chapter(-|_).*', url)
            chapNo = self.__getChapterNo(chapID.group())
            title = tag.text
            count += 1
            self.chapterList[count] = {
                'chapter-title' : title,
                'chapter-no' : chapNo
            }

    def mangakakalot(self):
        self.__request()
        count = 0

        if not self.single_url:
            # For finding Title of manga
            self.titleClass = self.parsedData.find(class_ = 'manga-info-text')
            self.__getTitleName()

            # For Getting Manga Poster
            self.posterClass = self.parsedData.find(class_ = 'manga-info-pic')
            self.__getMangaPoster()

        # Parsing Chapter List
        for i in self.parsedData.find_all(class_ = 'row')[1:]:
            a_tag = i.span.a
            url = a_tag['href']
            if not count and self.single_url:
                self.normUrl = url
                break
            chapID = re.search(r'chapter(-|_).*', url)
            chapNo = self.__getChapterNo(chapID.group())
            title = a_tag.text
            count += 1
            self.chapterList[count] = {
                'chapter-title' : title,
                'chapter-no' : chapNo
            }

    def __request(self):
        self.requestToWeb(f'{self.url}/{self.mangaID}')

    def __getTitleName(self):
        titleH1Tag = self.titleClass.h1
        self.title = titleH1Tag.text
    
    def __getMangaPoster(self):
        imgTag = self.posterClass.img
        self.posterUrl = imgTag['src']
    
    def __getChapterNo(self, chap_id:str):
        trimlist = chap_id.split('chapter')
        trimlead = trimlist[1]
        chapNo = trimlead[1:]
        return chapNo

