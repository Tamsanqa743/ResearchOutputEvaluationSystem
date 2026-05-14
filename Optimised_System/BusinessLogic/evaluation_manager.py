from .notification_service import notification_service
import json
from Benchmark.benchmark import benchmark

class evaluation_manager:

    def __init__(self, db_cursor):
        self.cursor = db_cursor
        self.score_arr = []
        self.notification_service = notification_service()


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
        
    def evaluate_submission(self, score_arr):
        average_score = (sum(score_arr)/len(score_arr)) # calculate average score
        consensus = bool(1) # not sure what this is supposed to do

        if average_score < 45:
            return 'rejected'
        elif (average_score > 45 and average_score < 60):
            return 'revision'
        elif average_score > 60:
            return 'accepted'
        
    @benchmark.track('start evaluation [optimized system]')
    def start_evaluation(self, reviewers, submission_id):

        decision = ''
        for reviewer in reviewers:
            reviewer_score = reviewer.submit_score()
            self.score_arr.append(reviewer_score)
            self.save_score(json.dumps(self.score_arr), submission_id )
            decision = self.evaluate_submission(self.score_arr)

        if decision == 'accepted':
            self.notification_service.send_notification(decision)
        elif decision == 'rejected':
            self.notification_service.send_notification(decision)
        elif decision == 'revision':
            self.notification_service.send_notification(decision)

        