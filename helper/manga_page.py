#!/usr/bin/env python3


### Importing Modules, Files, etc...
from helper.chapter import *


### Getting Page info
class ChapterPage():

    def __init__(self, manga_id):
        self.chapterObj = Chapter(manga_id, single_url = True)
        self.demoUrl = self.chapterObj.normUrl
        print(self.demoUrl)

