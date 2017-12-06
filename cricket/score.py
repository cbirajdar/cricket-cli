class LiveScore:
    def __init__(self, match_details):
        self.description = match_details['description']
        self.live = match_details['live']
        self.details = match_details['match']

    def is_international(self):
        if 'international_valid' in self.details:
            return self.details['international_valid'] == '1'
        return False

    def status(self):
        return self.live['status']

    def summary(self):
        if self.details['live_match'] == 'Y':
            return self.details['current_summary']
        return 'N/A'

    def location(self):
        return self.details['ground_name']
