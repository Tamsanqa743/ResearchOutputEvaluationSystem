import random

class evaluation_manager:

    def __init__(self, db_cursor):
        self.cursor = db_cursor

    def calaculate_average(self, scores):
        '''Calculate average score from provided scores'''
        average = 0
        for score in scores:
            average += score
        return (average/len(scores))

    def check_consensus(self, average_score):
        '''returns consensus on accpetance, rejection and revision'''
        if average_score < 45:
            return 'reject'
        elif (average_score > 45 and average_score < 60):
            return 'revision'
        elif average_score > 60:
            return 'accept'

    def apply_rules(self):
        '''rule check pass or fail'''
        return bool(random.randint(0,1))

    def notify_acceptance(self):
        pass

    def notify_rejection(self):
        pass

    def notify_revision(self):
        pass

    def save_score(self, final_score):
        try:    
            self.cursor.execute('''INSERT INTO research_output(score) VALUES (?)''', (final_score))
            self.db_connect.commit()
            return True
        except:
            return False
