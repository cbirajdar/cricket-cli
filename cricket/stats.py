import argparse
from .live_feed import LiveFeedParser
from .rankings import IccRankingsParser
from terminaltables import AsciiTable

LIVE_FEED_URL = 'http://static.cricinfo.com/rss/livescores.xml'
PLAYER_RANKINGS_URL = 'http://www.espncricinfo.com/rankings/content/page/211270.html'
TEAM_STANDINGS_URL = 'http://www.espncricinfo.com/rankings/content/page/211271.html'


def get_scores():
    live_feeds = LiveFeedParser(LIVE_FEED_URL).get_all_scores()
    # Sort scores to show international scores first
    live_feeds = sorted(live_feeds, key=lambda live_feed: ~live_feed.is_international())
    _print_scores(live_feeds)


def _print_scores(live_feeds):
    if len(live_feeds) == 0:
        print('No live matches at this time')
        return
    live_scores = []
    for feed in live_feeds:
        live_scores.append(['Match', feed.description])
        live_scores.append(['Status', feed.status()])
        live_scores.append(['Summary', feed.summary()])
        if feed != live_feeds[-1]:
            live_scores.append([])
    table = AsciiTable(live_scores)
    table.inner_row_border = True
    table.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
    print(table.table)


def get_rankings():
    rankings = _get_rankings_parser(PLAYER_RANKINGS_URL).player_rankings()
    for category, ranking in rankings.items():
        table = AsciiTable(ranking, category)
        print(table.table)


def get_standings():
    standings = _get_rankings_parser(TEAM_STANDINGS_URL).team_standings()
    for championship, standing in standings.items():
        table = AsciiTable(standing, championship)
        print(table.table)


def _get_rankings_parser(url):
    return IccRankingsParser(url)


# Based on: https://docs.python.org/2/library/argparse.html
def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    subparsers.add_parser('scores', help='Live cricket scores').set_defaults(func=get_scores)
    subparsers.add_parser('rankings', help='ICC player rankings').set_defaults(func=get_rankings)
    subparsers.add_parser('standings', help='ICC team standings').set_defaults(func=get_standings)
    return parser.parse_args()
