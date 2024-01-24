class Stats:  # отслеживание статистики

    def __init__(self):
        """gjktyjktyktkjmtr"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):  # статистика изменяющаяся во время игры
        self.guns_left = 2
        self.score = 0
        self.level = 0
