from .validator import validator
from .database_service import database_service
from .reviewer_manager import reviewer_manager
from .evaluation_manager import evaluation_manager
from .reviewer import reviewer
import json


class submission_service:

    def __init__(self):
        self.validator = validator()
        self.db_service = database_service()
        self.reviewer_manager = reviewer_manager()
        self.evaluation_manager = evaluation_manager(self.db_service.db_connect)
        self.final_reviewers = []

    def submit_data(self, combined_submission):
        if not self.validator.validate_format(combined_submission):
            return False, "Data Format Validation Failed"
        
        processed_data = json.loads(combined_submission)

        success, submission_id = self.db_service.save_submission(processed_data)

        if not success:
            return False, "Error Submitting. Try Again"

        reviewers = self.reviewer_manager.get_available_reviewers(processed_data)

        self.final_reviewers = []

        for reviewer_candidate in reviewers:
            reviewer_instance = reviewer(reviewer_candidate[0], reviewer_candidate[1], reviewer_candidate[2], reviewer_candidate[3])
            self.final_reviewers.append(reviewer_instance)
            reviewer_instance.assign_review(submission_id)

        self.evaluation_manager.start_evaluation(self.final_reviewers, submission_id)

        return True, submission_id