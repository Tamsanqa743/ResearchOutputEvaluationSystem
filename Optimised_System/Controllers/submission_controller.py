from BusinessLogic.submission_service import submission_service
from flask import flash

class submission_controller():
    def __init__(self):
        self.service = submission_service()

    def submit_data(self, combined_submission):
        success, result = self.service.submit_data(combined_submission)

        if success:
            flash("Submission Successful!", "success")
            return True
        else:
            flash(result, "danger")
            return False