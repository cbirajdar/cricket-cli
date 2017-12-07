import argparse
from colorclass import Color
from live_feed import LiveFeedParser
from rankings import IccRankingsParser
from terminaltables import AsciiTable

LIVE_FEED_URL = 'http://static.cricinfo.com/rss/livescores.xml'
PLAYER_RANKINGS_URL = 'http://www.espncricinfo.com/rankings/content/page/211270.html'
TEAM_STANDINGS_URL = 'http://www.espncricinfo.com/rankings/content/page/211271.html'


def get_scores():
    feed_parser = LiveFeedParser(LIVE_FEED_URL)
    live_feeds = feed_parser.get_international()
    if len(live_feeds) == 0:
        print('No live international matches at this time')
        return
    live_scores = []
    for feed in live_feeds:
        live_scores.append([Color('{red}Match{/red}'), feed.description])
        live_scores.append([Color('{green}Status{/green}'), feed.status()])
        live_scores.append([Color('{blue}Summary{/blue}'), feed.summary()])
    table = AsciiTable(live_scores)
    table.inner_row_border = True
    table.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
    print(table.table)


def get_rankings():
    rankings = IccRankingsParser(PLAYER_RANKINGS_URL).player_rankings()
    for category, ranking in rankings.iteritems():
        table = AsciiTable(ranking, category)
        print(table.table)


def get_standings():
    standings = IccRankingsParser(TEAM_STANDINGS_URL).team_standings()
    for championship, standing in standings.iteritems():
        table = AsciiTable(standing, championship)
        print(table.table)


# Based on: https://docs.python.org/2/library/argparse.html
def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    scores = subparsers.add_parser('scores', help='Live cricket scores')
    scores.set_defaults(func=get_scores)
    rankings = subparsers.add_parser('rankings', help='ICC player rankings')
    rankings.set_defaults(func=get_rankings)
    standings = subparsers.add_parser('standings', help='ICC team standings')
    standings.set_defaults(func=get_standings)
    return parser.parse_args()
