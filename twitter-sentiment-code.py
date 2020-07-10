# remove punctuation
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(strWord):
    for char in punctuation_chars:
        strWord = strWord.replace(char, "")
    return strWord


# get positive sentiment
def get_pos(strSentences):
    positive_words = []
    with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
    
    strSentences = strip_punctuation(strSentences)
    listSentences= strSentences.split()
    count=0
    for word in listSentences:
        word = word.lower()
        for positiveWord in positive_words:
            if word == positiveWord:
                count = count + 1
    return count


# get negative sentiment
def get_neg(strSentences):
    negative_words = []
    with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

    strSentences = strip_punctuation(strSentences)
    listSentences = strSentences.split()
    count = 0
    for word in listSentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count = count + 1
    return count


# open main twitter data file and write resulting data in a new file
outfile = open("project_twitter_data.csv", "r")
newfile = open("resulting_data.csv", "w")
newfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
newfile.write('\n')

lines = outfile.readlines() # read = entire file as a single string, readline = each line as a string, readlines = each line as an element in a list
header = lines.pop(0)
for row in lines:
    value = row.strip().split(',')
    netScore = (get_pos(value[0])) - (get_neg(value[0]))
    newfile.write("{}, {}, {}, {}, {}".format(value[1], value[2], get_pos(value[0]), get_neg(value[0]), netScore))
    newfile.write('\n')
print('The new file containing resulting data has been generated in .csv format!')

outfile.close()
newfile.close()
