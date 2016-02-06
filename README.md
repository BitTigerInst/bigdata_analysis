# bigdata_analysis
# discription
using spark to collect data from internet and do some analysis
# language
python
# plan
1. Download and Install Spark. 
2. Download Wikipedia dataset. Extract about 100 pages (items) based on your own interest. Can use snowball method to crawl a few related/linked pages. Create TF-IDF of each page.
3. Use Twitter Streaming API to receive real-time twitter data. Collect 30 mins of Twitter data on 5 companies using keyword=xxx (e.g., ibm). Consider all Twitter data from a company is one document. Create TF-IDF of each company’s tweets in that 30 minutes.
4. Use Yahoo Finance to receive the Stock price data. Collect 30 mins of Finance data on 5 companies, one value per minute. Use the outlier function to display outliers that are large than two standard deviation.

### owner
