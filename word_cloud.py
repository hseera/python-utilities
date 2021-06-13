# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

import warnings
warnings.filterwarnings("ignore")
 
def extract_data(file_name):
    
    try:
        tools_df = pd.read_csv(file_name)
        
        title_word_chart(tools_df['title'])
        
    except Exception as e:
        print(e)


    
def title_word_chart(title_list):
    text = (title_list.str.rstrip()).values
    wordcloud = WordCloud(width = 400, height = 200, random_state=1, background_color='salmon', colormap='Pastel1', 
                          collocations=False, stopwords = STOPWORDS).generate(" ".join(text)) # adds apostrophe if you use str(text) 
    
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud) 


def main():
    FILE_TO_READ = "./sample_files/title.csv"  # file containing column with tool names seperated by ", ". This is a demo file

    extract_data(FILE_TO_READ)

if __name__ == "__main__":
    main()
