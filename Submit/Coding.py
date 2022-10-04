#!/usr/bin/env python
# coding: utf-8

# # Data Preparation

# ### EDA

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


os = 'G:\Kumpulan Dataset\Astronomi'

star = pd.read_csv(os+'/map_object_list.csv')


# In[3]:


star


# In[4]:


star = star[['type','name', 'distance (parsecs)']]


# In[5]:


star.isna().sum()


# Data tidak memiliki data NaN dari 2557 data yang tersedia.

# In[6]:


df_new = star.copy()


# Setelah mengubah data dari list (dengan setiap panjang data ialah 2557) akan dimasukkan kedalam dataframe dalam bentuk dictionary dengan variable "astronom"

# ### Prepration Dataframe for modeling

# In[7]:


typee = df_new['type'].to_list()
name = df_new['name'].to_list()
distance = df_new['distance (parsecs)'].to_list()


# In[8]:


print(len(typee))
print(len(name))
print(len(distance))


# In[9]:


astronom = pd.DataFrame({
    'type' : typee,
    'name' : name,
    'distance' : distance
})


# In[10]:


astronom


# ### TF-IDF dan Cosine Similarity

# Disini akan melakukan **TF-IDF** untuk menghitung bobot dari setiap tipe menggunakan library sklearn

# In[11]:


from sklearn.feature_extraction.text import TfidfVectorizer


# Membuat variable baru dengan nama data yang menyimpan dataframe sebelumnya dan variable **tf** sebagai fungsi TF-IDF

# In[12]:


data = astronom


# In[13]:


tf = TfidfVectorizer()


# Melakukan extract dan get feature dari tipe planet yang ada pada data

# In[14]:


tf.fit(data['type'])

tf.get_feature_names()


# Setelah melakukan get feature yang tersedia, maka ditransformasikan menjadi kolom dan apabila di shape akan mendapatkan menjadi 2557 baris dan 7 kolom

# In[15]:


tfidf_matrix = tf.fit_transform(data['type'])

tfidf_matrix.shape


# In[16]:


tfidf_matrix.todense()


# In[17]:


pd.DataFrame(
            tfidf_matrix.todense(),
            columns=tf.get_feature_names(),
            index = data.name
            )


# In[18]:


from sklearn.metrics.pairwise import cosine_similarity


# In[19]:


cosine_sim = cosine_similarity(tf.fit_transform(data['type']))
cosine_sim


# In[20]:


cosine_sim_df = pd.DataFrame(cosine_sim, columns = data['name'], index = data['name'])
print('Shape:', cosine_sim_df.shape)


# In[21]:


cosine_sim_df.sample(10, axis=1).sample(5, axis=0)


# # Modeling 

# In[22]:


def planet_recommendations(name, similarity_data=cosine_sim_df, items= data[['name', 'type', 'distance']], k=10):
    index = similarity_data.loc[:,name].to_numpy().argpartition(
        range(-1, -k, -1))
    
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    closest = closest.drop(name, errors='ignore')
    
    return pd.DataFrame(closest).merge(items).head(k)


# In[23]:


data[data.name.eq('UBC 119')]


# # Evaluation

# In[24]:


result = planet_recommendations('UBC 119')
result


# In[25]:


relevant = len(result[result.type == 'open cluster'])
not_relevant = len(result[~(result.type == 'open cluster')])
items_total = len(result.type)


# In[26]:


accuracy = ((relevant + not_relevant)/items_total) * 100
precision = (relevant / items_total) * 100
recall = (relevant/(relevant + not_relevant)) * 100

print('Accuracy: {}%'.format(round(accuracy),0))
print('Precision: {}%'.format(round(precision),0))
print('Recall: {}%'.format(round(recall),0))

