import praw

def fetch_reddit_posts(client_id, client_secret, user_agent, subreddit_name, limit=5):
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    subreddit = reddit.subreddit(subreddit_name)
    return [{"title": post.title, "url": post.url} for post in subreddit.hot(limit=limit)]
