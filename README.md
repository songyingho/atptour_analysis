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

__Methodology__: This project uses <code>Python 3</code>, documented with <code>Jupyter Notebook</code>. Data was collected from web-scraping HTML pages using <code>requests</code> and <code>lxml</code> libraries. We then used a combination of <code>Numpy</code>, <code>Pandas</code> and <code>Sklearn</code> for data cleaning, filtering and feature engineering. 

Player Statistics were used for clustering models, namely <code>K-Means Clustering</code> and <code>Hierarchical Agglomerative Clustering</code>.<code>PCA</code> was used for dimensionality reduction, evaluation was conducted using both <code>Silhouette Score</code> and <code>Calinski-Harabasz Score</code>. 

Moving on to the matches data, preliminary feature selection was conducted with a combination of correlation matrix, variance inflation factor (VIF) and Decision Tree. A nested 5-fold cross validation within a train-validation-test split of 64:16:20 was employed for all our models. Feature Reduction and Hyperparameter Tuning using <code>GridSearchCV</code> was applied to the following tested models,<code>Logistic Regression</code>, <code>Decision Trees</code>, <code>Random Forest</code>, <code>AdaBoost</code> and <code>XGBoost</code>. Models were compared using the <code>ROC-AUC score</code>. Final trained models were saved using <code>Joblib</code> and visualizations were made using <code>Seaborn</code>.

__High Level Overview__: The project started by web scraping the ATPTour website, with 3 completely scraped dataset from 1990-2019. Individiual statistics of players with at least 50 wins are used for clustering to differentiate top players' playing style, strengths and weaknesses. Labels generated from clustering are then mapped onto the matches dataframe for further analysis. The datasets were then cleaned appropriately and merged into a single dataframe, ready for data analysis and modelling.

We then conducted initial data analysis and began feature reduction based on multicollinearity and feature importances. Next, we created learning models using Logistic Regression, Decision Trees, Random Forest, AdaBoost and XGBoost. Hyperparameters were then tuned using GridSearchCV. The process iterated with feature reduction, model training and hyperparameter optimization. With a predictive and an analysis model in mind, we finalized the number of features and conduct final model selection based on model robustness and validation AUC score. Model results with final selected model bolded shown in the tables below:

__For pre-match prediction model with 2 features:__
|        Model        | Train AUC | Validation AUC |
|:-------------------:|:---------:|:--------------:|
| Logistic Regression |   66.97   |      67.32     |
|    Decision Tree    |   84.95   |      76.68     |
|    Random Forest    |   84.93   |      76.75     |
|       AdaBoost      |   76.47   |      76.54     |
|     __XGBoost__     |   76.89   |    __76.73__   |

__For match analysis model with 6 features:__
|        Model        | Train AUC | Validation AUC |
|:-------------------:|:---------:|:--------------:|
| Logistic Regression |   73.50   |      73.66     |
|    Decision Tree    |   96.95   |      90.45     |
|    Random Forest    |   97.66   |      91.64     |
|     __AdaBoost__    |   92.53   |    __92.60__   |
|       XGBoost       |   92.88   |      92.49     |

The models were then used for a in-depth case study on Wimbledon 2019 Final, using the prediction model to predict match result based on historical data prior to the match and using the match analysis model to analyze player performance and momentum shift during the match. 

The models were also transformed into an executable python script, compatible to use on __Window's Command Prompt__ or __Mac's Terminal__ for an interactive experience for user wishing to test the 2 models developed in this project.

__Limitations__:
1. Clustering only used players with more than 50 wins on tour in a specific time period, there would be data leakage and this did not account for many lower level players with less than 50 wins, resulting in many missing values when the labels are mapped onto the main dataset.
2. Data used includes Best-Of-3 and Best-Of-5 Sets matches.

__Future Work__: 
1. Train surface-specific models to better predict and analyze match outcomes on different surfaces (e.g. Clay, Hard, Grass)
2. Train player-specific models to study specific strategy against a specific player
3. Create usable front end for the models created for user testing
4. Create an automated machine learning pipeline from web-scraping to model selection
5. Create new model for live odds tracking by inputting live match data points
