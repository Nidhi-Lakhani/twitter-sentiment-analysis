# twitter-sentiment-analysis
Twitter Sentiment Analysis - inspired by University of Michigan's Python 3 Programming Specialization on Coursera.

This project is a part of the final week project of the course 'Python Functions, Files and Directories' which is the second course in the Python 3 Programming Specialization by University of Michigan and provided on Coursera. The twitter data is a set of fake tweets, as provided in the course itself. The main project is divided into two parts - Twitter Sentiment Classifier and Twitter Sentiment Analysis.

   1. Twitter Sentiment Classifier:
   
This is the first step and it concerns with reading the set of tweet date and categorizing them as either positive or negative. This would be done by comparing the words in the twitter data file with the positive.txt file which contains positive words and the negative.txt file which contains a set of negative words. We will first define the function: 

    strip_punctuation() 
which will strip all kinds punctuations present in the tweets and we will get a set of pure words, stripped from all punctuations from the tweets. Then, we will define two main functions:
    
    get_pos()
which will give us the count of positive words and

    get_neg()
which will give us the count of negative words in the tweets. This will then be used to get the overall sentiment of a tweet. This first part will give us the data in which we have the sentiment of the tweets classified as positive or negative. In the next part, we will use this data to complete our project. 

   2. Twitter Sentiment Analysis:
   
In this part we will use the data obtained by executing the above functions to create a csv file, then open it with a spreadsheet program like Excel or Google Sheets to generate the final graph. We will open the project_twitter_data file which contains the twitter data and create resulting_data, get its positive and negative score, create a csv file which and add our data in it, which will be the final output. The open that resulting file and generate the graph.

    
