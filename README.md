# twitter-sentiment-analysis
Twitter Sentiment Analysis - inspired by University of Michigan's Python 3 Programming Specialization on Coursera.

This project is a part of the final week project of the course 'Python Functions, Files and Directories' which is the second course in the Python 3 Programming Specialization by University of Michigan and provided on Coursera. The twitter data is a set of fake tweets, as provided in the course itself. The main project is divided into two parts - Twitter Sentiment Classifier and Twitter Sentiment Analysis.

   1. Twitter Sentiment Classifier:
   
This is the first step and it concerns with reading the set of tweet data and categorizing them positve or negative. The task is to build a sentiment classifier, which will detect how positive or negative each tweet is. This would be done by comparing the words in the twitter data file with the positive.txt file which contains positive words and the negative.txt file which contains a set of negative words. We will first define the function: 

    strip_punctuation() 
which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. Then, we will define two main functions:
    
    get_pos()
 which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. The function should return a positive integer - how many occurrences there are of positive words in the text. All of the words in positive_words are lower cased, so we’ll need to convert all the words in the input string to lower case as well.

    get_neg()
which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. This will then be used to get the overall sentiment of a tweet. The function should return a positive integer - how many occurrences there are of negative words in the text. Again, all words in negative_words are lower cased, so we'll need to convert all the words in the input string to lower case.

This first part will give us the data in which we have the sentiment of the tweets classified as positive or negative. In the next part, we will use this data to complete our project. 

   2. Twitter Sentiment Analysis:
   
In this part we will use the data obtained by executing the above functions to create a csv file, then open it with a spreadsheet program like Excel or Google Sheets to generate the final graph. The project_twitter_data file has three columns - the actual tweet, number of retweets and number of replies. We will open the project_twitter_data file which contains the twitter data and create resulting_data.csv, get its positive and negative score and write data in it, which will be the final output. The final output should have the following data: Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. Then open that resulting file and generate the graph.

    
