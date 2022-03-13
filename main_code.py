import pandas as pd

df = pd.read_csv('data\\train.csv')
all_words = set()

for x in df['word1']:
    all_words.add(x)
for x in df['word2']:
    all_words.add(x)

all_words = list(all_words)
all_words.insert(0, '<None>')

df_vect = pd.read_csv('D:\My Python Stuff\Sanskrit NLP\ISCLS-19-master\data\\train.csv')

for i in range(len(df_vect['word1'])):
    df_vect['word1'][i] = all_words.index(df_vect['word1'][i])
for i in range(len(df_vect['word2'])):
    df_vect['word2'][i] = all_words.index(df_vect['word2'][i])
