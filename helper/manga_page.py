#!/usr/bin/env python3


### Importing Modules, Files, etc...
from helper.chapter import *
import base64


### Getting Page info
class ChapterPage(CommonThings):

    def __init__(self, manga_id, chapter_no):
        """
        Object initialising
        manga_id - str
        chapter_no - str
        """

        self.chapNo = chapter_no
        self.mangaID = manga_id

        self.xheader = {
            'referer' : 'https://readmanganato.com/'
        }

        super().__init__()    # Inheriting CommonThings class
        self.main()
    
    def getChapUrl(self, problem = False):
        """
        Getting original url of chapter
        for scrapping pages of that manga chapter
        """

        if problem:     # if manga_id is of 'read-' type(it has a different problem) 

            # For getting demo url, it will scrap urls from chapter list
            self.chapterObj = Chapter(self.mangaID, single_url = True)
            self.demoUrl = self.chapterObj.normUrl

            # Getting original url
            comUrl = re.search(r'.*chapter(-|_)', self.demoUrl)
            self.url = comUrl.group() + self.chapNo
        else:
            # Generating original url
            url = f'https://{self.domain}.com/'
            if self.domain == 'mangakakalot':
                url = url + 'chapter/'
            self.url = f'{url}{self.mangaID}/chapter{self.delimiter}{self.chapNo}'
    
    def main(self):
        """
        Running object
        """
        self.gettingDomain()
        self.__getPagesUrls()
    
    def gettingDomain(self):
        """
        Getting Domain of manga & then
        getting Orignal Url
        """
        if 'manga-' not in self.mangaID:
            self.domain = 'mangakakalot'
            if 'read-' in self.mangaID:
                """
                if it's problem url, in which manga id is something but
                on accessing chapter it changes it's manga id to it's
                manga title
                """
                self.getChapUrl(problem = True)
                return
            self.delimiter = '_'
        else:
            self.domain = 'readmanganato'
            self.delimiter = '-'
        self.getChapUrl()
    
    def __getPagesUrls(self):
        """
        Getting url of all pages of a chapter
        """
        self.requestToWeb(self.url)     # Requesting to web
        pageList = list()

        # Parsing Data to fetch url of all pages
        divTags = self.parsedData.find_all('div', class_ = 'container-chapter-reader')
        for imgTag in divTags[0].find_all('img'):
            pageList.append(imgTag['src'])
        self.pageList = pageList

