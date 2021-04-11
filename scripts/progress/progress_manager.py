import logging


class ProgressManager:

    def __init__(self, logger):
        self.logger = logger
        self.percentage_previous = 0.0
        self.step_current = 0.0
        self.step_total = 0.0
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_up(self, step_total):
        self.step_total = step_total

    def step(self):
        if self.active:
            self.step_current += 1
            self.calculate_progress()

    def calculate_progress(self):
        percentage_current = 0.0
        if not self.step_total == 0.0:
            percentage_current = self.step_current / self.step_total
        percentage_current *= 100
        percentage_diff = percentage_current - self.percentage_previous
        if percentage_diff > 1.0:
            self.percentage_previous = percentage_current
            assert isinstance(self.logger, logging.Logger)
            self.logger.info("Progress: " + str(int(percentage_current)) + "%")
