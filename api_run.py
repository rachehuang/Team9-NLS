
#pip install newsapi-python
from newsapi import NewsApiClient
import requests  
import pandas as pd
import math
import json
import datetime
from datetime import date, timedelta
from collections import defaultdict
import config

api = NewsApiClient(api_key=config.api_key)

class GatherArticles:

    def __init__(self, api, key_words):
        self.api_key = api
        self.key_words = key_words
        self.end_date = date.today() - timedelta(days = 29)


    def grab_articles(self):
        all_articles = self.api_key.get_everything(q=self.key_words, to= date.today(), from_param= self.end_date, page_size=100, page=1)
        with open('json_files/articles{}.json'.format(datetime.datetime.now().strftime("%Y%m%d")), 'w') as fp:
            json.dump(all_articles, fp)
            print(fp)
        print('Saved.')

if __name__ == '__main__':
    run = GatherArticles(api,'COVID OR Coronavirus')
    run.grab_articles()

