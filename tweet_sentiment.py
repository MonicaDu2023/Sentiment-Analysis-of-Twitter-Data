import sys


def create_sent_dict(sentiment_file):
 #A function that creates a dictionary which contains terms as keys and their sentiment score as value
    
   sentimentdict = open(sentiment_file, 'r')
    scores = {}
    for line in sentimentdict:
        term, score = line.split("\t")
        score[term] = int(score)
    return scores
  
def get_tweet_sentiment(tweet, sent_scores):
 #A function that find the sentiment of a tweet and outputs a sentiment score.

    score = 0
    sent_scores = create_sent_dict(sentiment_file)
    if "text" in tweet:
        words = tweet.split()
        for word in words:
            if word in sent_scores:
                score = score + sent_scores[word] 
    return score

def get_sentiment(tweets_file, sent_scores, output_file):
 #A function that finds the sentiment of each tweet and outputs a sentiment score (one per line).

    tweets = open(tweets_file, 'r')
    output = open(output_file, 'w')
    for tweet in tweets:
        score = get_tweet_sentiment(tweet, sent_scores)
        output.write('%d\n' % score)
    output.close()
    tweets.close()


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]
    output_file = "sentiment.txt"

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)
    # Read the tweet data and assign sentiment
    get_sentiment(tweets_file, sent_scores, output_file)


if __name__ == '__main__':
    main()
