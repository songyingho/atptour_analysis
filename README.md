# Analysis of ATP Tour Matches from 1990 - 2019 with Machine Learning Models

_Work by Song Ying Ho_

__Executive Summary__: 

In this project, we accomplished the following:
1. Web Scraping from [ATPTour Official Website](https://www.atptour.com)
2. Data Cleaning for Clustering
3. Optimization of Clustering Models (Final Silhouette Score: 0.88)
4. Data Cleaning & Feature Engineering for Classification
5. Exploratory Data Analysis (EDA)
6. Test & Optimization of Multiple Classification Models
7. Final Model Selections with Feature Reduction
8. Developed 2 models:
  * Pre-match Prediction Model (XGBoost using 2 features with Validation AUC: 76.73 %)
  * Match Analysis Model (AdaBoost using 6 features with Validation AUC: 92.60 %)
9. Case Study on Wimbledon 2019 Final
10. Developed .py script for Interactive User Testing

__Data Source__: Data mostly web-scraped from [ATPTour](https://www.atptour.com), with supplement information from [UltimateTennisStatistics](https://www.ultimatetennisstatistics.com) and [FlashScore](https://www.flashscore.com/match/fyXBxdlb/#match-statistics) for case study.

__Files__: 
* [index](./index.ipynb): main Jupyter Notebook
* [prediction](./prediction.pkl): Trained model for pre-match prediction
* [analysis](./analysis.pkl): Trained model for match analysis
* [index_csv](./index_csv): Contains all the csv used by index.ipynb
* [csv_source](./csv_source): Contains all notebooks for Web Scraping & Data Cleaning
* [clustering](./clustering): Contains notebook for clustering models
* [user_cmd_test](./cmd_testing/user_cmd_test.py): .py file contaning final models, compatible to use on cmd

__Methodology__:

__High Level Overview__:

__Limitations__:

__Future Work__:
