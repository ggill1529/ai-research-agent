import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    return [{"title": entry.title, "summary": entry.summary, "link": entry.link} for entry in feed.entries]
