import json

import feedparser
import grequests

from score import LiveScore


class LiveFeedParser:
    def __init__(self, rss_url):
        self.url = rss_url

    def get_all(self):
        response = feedparser.parse(self.url)
        match_feeds = response['entries']
        live_scores = []
        responses = (grequests.get(match_feed['id'].replace('html', 'json')) for match_feed in match_feeds)
        for response in grequests.map(responses):
            match = json.loads(response.content)
            live_score = LiveScore(match)
            live_scores.append(live_score)
        return live_scores

    def get_international(self):
        return [live_score for live_score in self.get_all() if live_score.is_international()]
