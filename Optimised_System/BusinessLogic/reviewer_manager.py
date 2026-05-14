from .database_service import database_service
class reviewer_manager:

    def __init__(self):
        self.database_service = database_service()
        self.max_reviews_assigned = 5


    def get_available_reviewers(self, submission):
        '''get all available reviewers'''
        all_reviewers = self.database_service.fetch_reviewers()
        final_reviewers = []

        for reviewer in all_reviewers:
            # filter based on author name
            if reviewer[1] not in submission['author']:
                if reviewer[2] < self.max_reviews_assigned:
                    final_reviewers.append(reviewer)
        return final_reviewers