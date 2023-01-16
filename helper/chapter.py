#!/usr/bin/env python3


### Importing Modules, Files, etc...
from helper.common import *

key_lst = ['name', 'thumbnail', 'status', 'description']

### Getting a List of Chapters
class Chapter(CommonThings):

    def __init__(self, manga_id, single_url=False):
        self.mangaID = manga_id
        self.single_url = single_url
        self.manga_info = dict()
        super().__init__()    # Inheriting CommonThings class
        self.gettingChapters()
        
    
    def gettingChapters(self):
        """
        Getting Chapters name and id
        """
        self.requestToWeb(f'https://api.mangaowl.to/v1/stories/{self.mangaID}')
        
        jsonData = json.loads(self.webcontent)
        for key in key_lst:
            self.manga_info[key] = jsonData[key]
        self.manga_info['author_name'] = jsonData['authors'][0]['name']
        self.manga_info['genres'] = list(x['name'] for x in jsonData['genres'])
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
