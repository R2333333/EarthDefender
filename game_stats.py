class GameStats():
    """docstring for GameStats."""

    def __init__(self, settings):
        #initialize game statics
        self.settings = settings
        self.reset_stats()
        self.active = False

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
