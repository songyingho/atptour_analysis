# Data Cleaning

__This folder contains all documents used for data cleaning and all version of CSV produced by the data cleaning process.__

__Cleaned Datasets__:
1. [Version 1](./clean_df_v1.0.csv) - Merged tournament csv with matches csv and removed null values and unusual data points
2. [Version 2](./clean_df_v2.0.csv) - Built on Version 1, performed feature engineering and added additional metrics for analysis with reorganized columns. __Dataframe Shape: 92159 rows x 95 columns__. Each row contains a match with individual statistics for winner and loser.
3. [Version 3](./clean_df_v3.0.csv) - Built on Version 2, the matches are separated into 2 rows of individual statistics with an added label 'winner' with boolean values to describe the outcome of the match for the player. __Dataframe Shape: 184318 rows x 52 columns__. Each row contains an individual player statistics for a match.

Original scraped data can be found in [Web Scaping](https://github.com/songyingho/atptour_analysis/tree/master/csv_source/web_scraping)
