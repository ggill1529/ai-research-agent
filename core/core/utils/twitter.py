# Twitter scraping placeholder (snscrape handles Twitter scraping externally)

import snscrape.modules.twitter as sntwitter

def fetch_tweets(query, limit=5):
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) >= limit:
            break
        tweets.append({"content": tweet.content, "url": tweet.url})
    return tweets
