class StatusCode5XX(Exception):
    def __init__(self, text):
        self.txt = text
