# Netflix Data Analysis Project

## Overview
This project analyzes Netflix data, focusing on various attributes such as movie release dates, genres, popularity, and vote averages. The analysis is performed using Python and visualized with Matplotlib and Seaborn.



### 1. `netflix_data_analysis.csv`
This CSV file contains the following columns:

- **Release Date**: Date when the movie was released.
- **Title**: Title of the movie.
- **Genre**: Genre of the movie.
- **Overview**: Brief description of the movie.
- **Popularity**: Popularity score of the movie.
- **Vote Count**: Number of votes received.
- **Vote Average**: Average rating of the movie.
- **Original Language**: Language in which the movie was originally produced.
- **Poster URL**: Link to the movie's poster.

#### Sample Data
![image alt](https://github.com/Ishan-dgt/Netflix_data_analysis/blob/main/Sample_data.png)
### 2. `Netflix_Data_Analysis.py`
This Python script performs the following tasks:

- **Data Loading**: Loads the CSV file into a Pandas DataFrame.
- **Data Cleaning**: 
  - Converts the **Release Date** to datetime format and extracts the year.
  - Drops unnecessary columns: **Overview**, **Original Language**, **Poster URL**.
  - Handles missing values.
- **Categorizing Vote Average**: Categorizes the **Vote Average** into four labels: `not_popular`, `below_avg`, `average`, `popular`.
- **Genre Processing**: Splits genres into a list and explodes the DataFrame to have one genre per row.
- **Data Visualization**: 
  - Plots the most frequent genres.
  - Plots the distribution of vote averages.
  - Identifies the movies with the highest and lowest popularity.
  - Displays a histogram of movie release dates.

#### Key Code Snippets
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/ISHAN DASGUPTA/Downloads/netflix_data_analysis.csv')

# Data Cleaning
df['Release Date'] = pd.to_datetime(df['Release Date'], dayfirst=True, errors='coerce')
df['Release Date'] = df['Release Date'].dt.year
df.drop(['Overview', 'Original Language', 'Poster URL'], axis=1, inplace=True)

# Categorizing Vote Average
def categorize_col(df, col, labels):
    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]
    df[col] = pd.cut(df[col], edges, labels=labels, duplicates='drop')
    return df

labels = ['not_popular', 'below_avg', 'average', 'popular']
categorize_col(df, 'Vote Average', labels)
```

### 3. Output Images
The following images are generated from the analysis:

- **Genre Distribution**:
  
  ![image alt](https://github.com/Ishan-dgt/Netflix_data_analysis/blob/main/output%201.png)
- **Vote Distribution**:
  
  ![image alt](https://github.com/Ishan-dgt/Netflix_data_analysis/blob/main/output%202.png)
- **Release Date Distribution**:
  
  ![image alt](https://github.com/Ishan-dgt/Netflix_data_analysis/blob/main/output%203.png)

## Key Findings
- The most frequent genre of movies released on Netflix.
- The movie with the highest popularity and its genre.
- The movie with the lowest popularity and its genre.
- The year with the most filmed movies.

## Conclusion
This analysis provides insights into Netflix's movie offerings, highlighting trends in genres, popularity, and release patterns. The visualizations help in understanding the distribution of various attributes effectively.

## Future Work
- Extend the analysis to include more recent data.
- Explore viewer demographics and their impact on movie ratings.
- Analyze trends over time in genres and popularity.
