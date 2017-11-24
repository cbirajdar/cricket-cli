import json
import requests
import feedparser
from model.score import LiveScore


class LiveFeedParser:
    def __init__(self, rss_url):
        self.url = rss_url

    def get_all(self):
        response = feedparser.parse(self.url)
        match_feeds = response['entries']
        live_scores = []
        for match_feed in match_feeds:
            response = requests.get(match_feed['id'].replace('html', 'json'))
            match = json.loads(response.content)
            live_score = LiveScore(match_feed['summary'], match['match'])
            live_scores.append(live_score)
        return live_scores

    def get_international(self):
        return [live_score for live_score in self.get_all() if live_score.is_international()]


feed_parser = LiveFeedParser('http://static.cricinfo.com/rss/livescores.xml')
for score in feed_parser.get_international():
    print (score.description + '\t' + score.summary()).expandtabs(10)
