import json

import feedparser
import grequests

from score import LiveScore


class LiveFeedParser:
    def __init__(self, rss_url):
        self.url = rss_url

    def get_all_scores(self):
        response = feedparser.parse(self.url)
        match_feeds = response.get('entries', [])
        live_scores = []
        responses = (grequests.get(match_feed['id'].replace('html', 'json')) for match_feed in match_feeds)
        for summary, response in zip(match_feeds, grequests.map(responses)):
            match = json.loads(response.content)
            match['summary'] = summary['summary_detail']['value']
            live_score = LiveScore(match)
            live_scores.append(live_score)
        return live_scores

    def get_international_scores(self):
        return [live_score for live_score in self.get_all_scores() if live_score.is_international()]
