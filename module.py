import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import difflib
from sklearn.metrics.pairwise import cosine_similarity

df9 = pd.read_csv('Final.csv')
def getindex(given_id):
    for i in range(len(df9)):
        if df9['id'][i] == given_id:
            return i


movies_list = df9['title_x'].to_list()
vector = TfidfVectorizer()
combined_data = df9['genres'] + ' ' + df9['keywords'] + ' ' + df9['tagline'] + ' ' + df9['cast'] + ' ' + df9['directors']
features = vector.fit_transform(combined_data.astype('U'))
similarity = cosine_similarity(features)

def find_movie(movie_name):
    try:


        movie_name_crrt = difflib.get_close_matches(movie_name,movies_list)[0]
        movie_id = df9[df9['title_x'] == movie_name_crrt].values[0][3]
        index_of_the_movie = getindex(movie_id)
        score_of_similarity = list(enumerate(similarity[index_of_the_movie]))
        similar_movies_list = sorted(score_of_similarity,key=lambda x:x[1],reverse=True)[:12]
        final_output = []
        for i in similar_movies_list:
            final_output.append([df9.iloc[i[0]]['title_x'],df9.iloc[i[0]]['directors'],df9.iloc[i[0]]['release_date']])
        return final_output
    except:
        return [['None','None','None']]

if __name__ == '__main__':
    print('Welcome to the Module Page')

