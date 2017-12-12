import unittest

from cricket.live_feed import LiveFeedParser
from cricket.stats import LIVE_FEED_URL


class LiveFeedParserTestCase(unittest.TestCase):
    def test_get_all_scores(self):
        live_scores = LiveFeedParser(LIVE_FEED_URL).get_all_scores()
        self._assert_scores(live_scores)

    def test_get_international_scores(self):
        live_scores = LiveFeedParser(LIVE_FEED_URL).get_international_scores()
        self._assert_scores(live_scores)

    def _assert_scores(self, live_scores):
        for live_score in live_scores:
            self.assertIsNotNone(live_score.description)
            self.assertIsNotNone(live_score.status())
            self.assertIsNotNone(live_score.summary())
