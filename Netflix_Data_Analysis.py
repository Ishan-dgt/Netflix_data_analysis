#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('/Users/ISHAN DASGUPTA/Downloads/netflix_data_analysis.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df['Genre'].head()


# In[6]:


df.duplicated().sum()


# In[7]:


df.describe()


# In[8]:


df.head()


# In[9]:


df['Release Date'] = pd.to_datetime(df['Release Date'], dayfirst=True, errors='coerce')

print(df['Release Date'].dtypes)


# In[10]:


df['Release Date'] = df['Release Date'].dt.year

df['Release Date'].dtypes


# In[11]:


df.head()


# Dropping the columns

# In[12]:


cols = ['Overview','Original Language','Poster URL']


# In[13]:


df.drop(cols, axis = 1, inplace = True)
df.columns


# categorizing Vote_Average column
# 
# We would the Vote_Average values and make 4 categories:popular average below_avg not_popular to describe it more using categorize_col() function provided above.

# In[14]:


def categorize_col(df, col, lebels):

    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]

    df[col] = pd.cut(df[col], edges , labels = labels, duplicates = 'drop')
    return df


# In[15]:


labels = ['not_popular', 'below_avg','average','popular']
categorize_col(df, 'Vote Average', labels)
df['Vote Average'].unique()


# In[16]:


df.head()


# In[17]:


df['Vote Average'].value_counts()


# In[18]:


df.dropna(inplace = True)

df.isna().sum()


# In[19]:


df.head()


# # we'd split genres into a list and then explode our dataframe to have only one genre per row for ezch movie

# In[20]:


df['Genre'] = df['Genre'].str.split(',')
df = df.explode('Genre').reset_index(drop = True)
df.head()


# In[21]:


#casting column into cateogy

df['Genre'] = df['Genre'].astype('category')

df['Genre'].dtypes


# In[22]:


df.info()


# In[23]:


df.nunique()


# In[24]:


df.head()


# # Data Visualization

# In[25]:


sns.set_style('whitegrid')


# # What is the most frequent genre of movies released on Netflix?

# In[26]:


df['Genre'].describe()


# In[27]:


sns.catplot(y = 'Genre', data = df, kind = 'count',
            order = df['Genre'].value_counts().index,
            color = '#4287f5')
plt.title('Genre column distribution')
plt.show()


# # Which has highest votes in vote avg column?

# In[28]:


df.head()


# In[29]:


sns.catplot(y = 'Vote Average', data = df, kind = 'count',
            order = df['Vote Average'].value_counts().index,
            color = '#4287f5')
plt.title('Votes distribution')

plt.show()


# # What movie got the highest popularity? What's its genre?

# In[30]:


df.head(2)


# In[31]:


df[df['Popularity'] == df['Popularity'].max()]


# # What movie got the lowest popularity? What's its genre?

# In[32]:


df[df['Popularity'] == df['Popularity'].min()]


# # Which year has the most filmmed movies?

# In[33]:


df['Release Date'].hist()
plt.title('Release Date column distribution')
plt.show()

