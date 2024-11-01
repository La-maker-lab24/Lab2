class Settings:
    def __init__(self, finish_score=8):
        self.finish_score = finish_score

    def update_finish_score(self, new_score):
        if new_score > 0:
            self.finish_score = new_score
        else:
            raise ValueError("Граница должна быть выше 0!")

    def get_finish_score(self):
        return self.finish_score

    def reset_finish_score(self):
        self.finish_score = 8


class AdvancedSettings(Settings):
    def __init__(self, finish_score=8, time_limit=30):
        super().__init__(finish_score)
        self.time_limit = time_limit

    def update_time_limit(self, new_time):
        if new_time > 0:
            self.time_limit = new_time
        else:
            raise ValueError("Временное ограничение должно быть выше 0!")

    def get_time_limit(self):
        return self.time_limit

    def reset_time_limit(self):
        self.time_limit = 30
