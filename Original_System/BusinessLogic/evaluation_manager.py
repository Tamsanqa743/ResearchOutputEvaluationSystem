from BusinessLogic.notification_service import notification_service
import json
from Benchmark.benchmark import benchmark

class evaluation_manager:

    def __init__(self, db_cursor):
        self.cursor = db_cursor
        self.score_arr = []
        self.notification_service = notification_service()

    def calaculate_average(self, scores):
        '''Calculate average score from provided scores'''
        average = 0
        for score in scores:
            average += score
        return (average/len(scores))

    def check_consensus(self):
        '''check consensus'''
        return True

    def apply_rules(self, average_score):
        '''returns consensus on accpetance, rejection and revision'''
        if average_score < 45:
            return 'rejected'
        elif (average_score > 45 and average_score < 60):
            return 'revision'
        elif average_score > 60:
            return 'accepted'


    def save_score(self, scores, research_id):
        try:    
            self.cursor.execute('''UPDATE reviews
            SET scores = ?
            WHERE research_id = ?
            ''', (scores, research_id))
            self.cursor.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    @benchmark.track('start evaluation flow [original system]')    
    def start_evaluation(self, reviewers, submission_id):

        decision = ''
        for reviewer in reviewers:
            reviewer_score = reviewer.submit_score()
            self.score_arr.append(reviewer_score)
            self.save_score(json.dumps(self.score_arr), submission_id )
            average_score = self.calaculate_average(self.score_arr)
            consensus = self.check_consensus() # not sure what this is supposed to do
            decision = self.apply_rules(average_score) 

        if decision == 'accepted':
            self.notification_service.notify_acceptance()
        elif decision == 'rejected':
            self.notification_service.notify_rejection()
        elif decision == 'revision':
            self.notification_service.notify_revision()

        