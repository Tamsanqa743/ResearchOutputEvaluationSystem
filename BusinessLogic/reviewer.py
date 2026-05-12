import random
class reviewer:

    def __init__(self, id, name, field_of_study):
        self.name = name
        self.id = id
        self.workload = 0
        self.field = field_of_study
        self.reviews = []


    def submit_score(self):
        '''Return score for review'''
        return random.rand(10, 100)
    
    def assign_review(self, research_id):
        reviewer_workload += 1
        self.reviews.append(research_id)


        '''Assign reviewer'''
        self.cursor.execute("""
            UPDATE research
            SET assigned_reviewer_id = ?
            WHERE id = ?
            """, (self.id, research_id))

        # update reviewer workload on db
        self.cursor.execute("""
            UPDATE reviewers
            SET workload = ?
            WHERE id = ?
            """, (reviewer_workload, id))

        self.db_connect.commit() # save changes