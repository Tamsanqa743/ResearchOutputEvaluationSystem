from flask import flash

class notification_service:

    def __init__(self):
        self.friendly_messages = {'accepted': "Congratulations!! Your research has been accepted!", 'rejected': "Unfortunately your research has been rejected!", 'revision': 'Research needs revisons!'}


    def send_notification(self, outcome_status):
        flash(self.friendly_messages[outcome_status], 'warning')