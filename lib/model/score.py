class LiveScore:
    def __init__(self, description, details):
        self.description = description
        self.details = details

    def is_international(self):
        return 'international_valid' in self.details and self.details['international_valid'] == '1'

    def summary(self):
        return self.details['current_summary']
