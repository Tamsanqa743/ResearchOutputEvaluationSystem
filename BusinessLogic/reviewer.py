import random
class reviewer:

    def __init__(name, self):
        self.reviewer_id = name
        self.workload = 0

    def submit_score(self):
        '''Return score for review'''
        return random.rand(10, 100)