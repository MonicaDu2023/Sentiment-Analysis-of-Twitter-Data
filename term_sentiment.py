import sys

def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
        """
    #open file and create dictionary
    with open(sentiment_file) as sentimentdict:
        scores = {}
        #use loop to read file into dictionary about score
        for line in sentimentdict:
            term, score = line.split("\t")
            scores[term] = int(score)
    return scores

def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.

            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict

            Returns:
                score (numeric): The sentiment score of the tweet
        """
    #initial score
    score = 0
    words = tweet.split()
    #add up score when word in tweet exist in dictionary we create
    for word in words:
        if word in sent_scores:
            score = score + sent_scores[word]
    return score

def term_sentiment(sent_scores, tweets_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

            Args:
                sent_scores (dictionary): A dictionary with terms and their scores (the output of create_sent_dict)
                tweets_file (string): The name of a txt file that contain the clean tweets
            Returns:
                dicitonary: A dictionary with schema d[new_term] = score
            """
    #create dictionary for new words
    new_term_sent = {}
    # read file in
    tweets = open(tweets_file, 'r')
    # read each tweet 
    for tweet in tweets:
        #initial several elements
        score = 0
        sentiment_num = 0
        average_sentimentscore = 0
        words = tweet.split()
        #add up score when word in tweet exist in old dictionary we create
        for word in words:
            word.lower()
            if word in sent_scores:
                sentiment_num = sentiment_num + 1
                score = score + sent_scores[word]
            # add up score when word in new dict we create
            elif word in new_term_sent:
                sentiment_num = sentiment_num + 1
                score = score + new_term_sent[word]
            # calculate each tweet average score
            if sentiment_num > 0:
                average_sentimentscore = score/ sentiment_num
            # set word not in old dict to average score in each tweet in new dict
            for word in words:
                word.lower()
                if word not in sent_scores:
                    new_term_sent[word] = average_sentimentscore 
    return new_term_sent


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)

    # Derive the sentiment of new terms
    new_term_sent = term_sentiment(sent_scores, tweets_file)

    for term in new_term_sent:        
        print(term, new_term_sent[term])


if __name__ == '__main__':
    main()
