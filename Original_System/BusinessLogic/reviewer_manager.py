import json
class reviewer_manager:

    def __init__(self,db_cursor):
        self.cursor = db_cursor


    def fetch_reviewers(self):
        self.cursor.execute("SELECT * FROM reviewers")
        reviewers = self.cursor.fetchall() # fetch all reviewers
        return reviewers # list of reviewers
    
    def filter_conflicts(self, reviewer_list, research_output):
        final_reviewers = []
       
        research_output = json.loads(research_output)
        for reviewer in reviewer_list:
            # filter based on author name
            if reviewer[1] not in research_output['author']:
                final_reviewers.append(reviewer)
        return final_reviewers

    def check_workload(self, reviewer_list):
        '''check workload of each reviewer and return filtered reviewer list'''
        final_reviewer_list = []
        max_reviews_assigned = 5 # max number of allowed review work per reviewer
        for reviewer in reviewer_list:
            # check reviewer workload
            if reviewer[2] < max_reviews_assigned:
                final_reviewer_list.append(reviewer)

        return final_reviewer_list
    
    def get_available_reviewers(self, submission):
        '''get all available reviewers'''
        all_reviewers = self.fetch_reviewers()
        filtered_reviwers = self.filter_conflicts(all_reviewers, submission)
        available_reviewers = self.check_workload(filtered_reviwers)

        return available_reviewers