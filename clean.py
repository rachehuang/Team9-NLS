import requests
import config
import json
import pandas as pd
from newspaper import Article
import nltk

nltk.download('punkt')

def scrape(df):
    new_df = df.set_index(['url'])
    new_df['html'] = None
    new_df['key_words'] = None
    for url in new_df.index:
        article = Article(url, language="en")
        article.download() 
        article.parse() 
        article.nlp() 
        new_df['html'].loc[url] = article.text
        new_df['key_words'].loc[url] = article.keywords 
    df = new_df.reset_index()
    return df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input file (CSV)')
    parser.add_argument('output', help='contents file (CSV)')
    args = parser.parse_args()
    
    df = pd.read_csv(args.input)
    df = df.drop_duplicates(subset=['title'])
    df = df.drop(['Unnamed: 0'], axis=1)
    contents = scrape(df)
    contents.to_csv(args.output, index=False)  