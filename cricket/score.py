class LiveScore:
    def __init__(self, match_details):
        self.description = match_details['description']
        self.live = match_details['live']
        self.details = match_details['match']
        self.summary = match_details['summary']

    def is_international(self):
        if 'international_valid' in self.details:
            return self.details['international_valid'] == '1'
        return False

    def current_summary(self):
        return self.details.get('current_summary', self.summary)

    def status(self):
        return self.live['status']

    def location(self):
        return self.details['ground_name']
