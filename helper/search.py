#!/usr/bin/env python3


### Importing Modules, Files, etc.
from urllib import request as req

class SearchEngine:

    def __init__(self, query):
        self.query = query
        self.searchingResult()
    
    def searchingResult(self):
        r = req.urlopen(f'https://mangakakalot.com/search/story/{self.query}')
        print(r)
