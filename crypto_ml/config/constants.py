from singleton_decorator import singleton


@singleton
class Constants:
    def __init__(self):

        # General constants
        self.SECONDS_IN_DAY = 86400

