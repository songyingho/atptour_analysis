# Web Scraping

__This folder contains all documents used for web scraping and all dataset scraped from external sources.__

Data Source: [ATP Tour](https://www.atptour.com/)

__Final Scraped Documents:__
1. [Tournament CSV](https://github.com/songyingho/atptour_analysis/tree/master/csv_source/web_scraping/tournaments_1990-2019.csv)
2. [Match Stats CSV](https://github.com/songyingho/atptour_analysis/tree/master/csv_source/web_scraping/match_stats_1990-2019.csv)
3. [Player Stats CSV](https://github.com/songyingho/atptour_analysis/tree/master/csv_source/web_scraping/player_stats_1990-2019.csv)

A brief on each CSV scraped will be described below and more technical details on Web Scraping can be found in [Web Scraping Notebook](https://github.com/songyingho/atptour_analysis/tree/master/csv_source/web_scraping/web_scraping.ipynb)

## Tournament CSV
An example of URL to scrape will be shown below:
<img src = 'https://github.com/songyingho/atptour_analysis/tree/master/csv_source/web_scraping/screenshots/tournaments_example.PNG'>

From the webpage, we obtained the following:
1. Tournament Name
2. Tournament ID
3. Tournament Type
4. Tourmanent Location
5. Tournament Start Date
6. Tournament Conditions
7. Tournament Surface

The web-scraping function built was then used to iterate from year 1990 to 2019, collecting all tournament information for the time period.


## Matches CSV
An example of URL to scrape will be shown below:
<img src = 'https://github.com/songyingho/atptour_analysis/tree/master/csv_source/web_scraping/screenshots/stats_example.PNG'>

From the webpage, we obtained all the raw values available in the picture above. 
The web-scraping function built was then used to iterate over every tournament in every year from 1990 to 2019.


## Players CSV
An example of URL to scrape will be shown below:
<img src = 'https://github.com/songyingho/atptour_analysis/tree/master/csv_source/web_scraping/screenshots/player_stats_example.PNG'>

From the webpage, we obtained the following:
1. Player ID
2. Height
3. Weight
4. Service Game Statistics
5. Return Game Statistics
6. Break Point Statistics

Using the matches CSV we scraped previously, [data engineering work](https://github.com/songyingho/atptour_analysis/tree/master/ipynb_archives/slug_id_pairings) was done to collect players with at least 50 wins during the 1990-2019 period, and this web-scraping function was iterated over the list of players collected. 
