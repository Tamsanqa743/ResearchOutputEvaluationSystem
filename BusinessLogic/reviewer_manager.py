import random

class reviewer_manager:

    def __init__(self,db_cursor):
        self.cursor = db_cursor


    def fetch_reviewers(self):
        self.cursor.execute("SELECT * FROM reviewers")
        reviewers = self.cursor.fetchall() # fetch all reviewers
        return reviewers # list of reviewers
    
    def filter_conflicts(self, reviewer_list):
        final_reviewers = []
        for reviewer in reviewer_list:
            if reviewer.name not in 'author':
                final_reviewers.append(reviewer)
        return final_reviewers

    def check_workload(self, reviewer_list):
        '''check workload of each reviewer and return filtered reviewer list'''
        final_reviewer_list = []
        max_reviews_assigned = 3 # max number of allowed review work per reviewer
        for reviewer in reviewer_list:
            if reviewer.workload < max_reviews_assigned:
                final_reviewer_list.append(reviewer)

        return final_reviewer_list
