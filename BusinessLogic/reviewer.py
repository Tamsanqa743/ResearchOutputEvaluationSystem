import random
class reviewer:

    def __init__(self, id, name, workload, field_of_study):
        self.name = name
        self.id = id
        self.workload = workload
        self.field = field_of_study
        self.review = 0


    def submit_score(self):
        '''Return score for review'''
        return random.randint(10, 100)
    
    def assign_review(self, research_id):
        self.workload += 1
        self.review = (research_id)